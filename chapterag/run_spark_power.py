from datasets import load_dataset
from dotenv import load_dotenv
import os
import tiktoken
import re
import requests
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf, PandasUDFType
import time

# Start time
start_time = time.time()

spark = SparkSession.builder \
    .appName("Parallel LLM Question Answering") \
    .getOrCreate()


# Load environment variables
load_dotenv()



def get_completion(prompt):
    url = "https://inference-api.netmind.ai/inference-api/v1/gemma-2-9b"
    
    # Define the payload
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stop_strings": "",
        "max_new_tokens": 2048,
        "temperature": 0.6,
        "top_p": 0.9,
        "top_k": 50,
        "repetition_penalty": 1.2
    }
    
    # Set headers
    headers = {
        "Authorization": api_token,
        "Content-Type": "application/json"
    }
    
    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Check the response status and extract the answer
    if response.status_code == 200:
        response_data = response.json()
        answer = response_data['choices'][0]['message']['content']
        return answer
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
        return None




def chunk_text_by_paragraph(text, min_tokens=500, max_tokens=1000, encoding_name='cl100k_base'):
    """
    Chunk text by tokens.

    :param text: The input text to chunk.
    :param min_tokens: Minimum number of tokens per chunk.
    :param max_tokens: Maximum number of tokens per chunk.
    :param encoding_name: Encoding name for the tokenizer.
    :return: List of text chunks.
    """
    enc = tiktoken.get_encoding(encoding_name)
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = []
    current_tokens = 0

    for paragraph in paragraphs:
        if not is_valid_sentence(paragraph):
            continue
        paragraph_tokens = len(enc.encode(paragraph))

        if current_tokens + paragraph_tokens > max_tokens:
            if current_tokens >= min_tokens:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = [paragraph]
                current_tokens = paragraph_tokens
            else:
                current_chunk.append(paragraph)
                current_tokens += paragraph_tokens
        else:
            current_chunk.append(paragraph)
            current_tokens += paragraph_tokens

    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))

    return chunks

def is_valid_sentence(sentence):
    # Define a regex pattern for a valid sentence
    valid_pattern = r'^[A-Z].*'
    invalid_pattern_bar = r'\| *\|'
    invalid_pattern_doi = r'https://doi'

    is_valid = bool(re.match(valid_pattern, sentence))
    contains_invalid_bar = bool(re.search(invalid_pattern_bar, sentence))
    contains_invalid_doi = bool(re.search(invalid_pattern_doi, sentence))

    return is_valid and not (contains_invalid_bar or contains_invalid_doi)

def generate_response(document):
    prompt = f"""
    ---Role---

    You are a helpful assistant responding to a question based on the provided reference paragraph and your own knowledge.

    ---Goal---

    1. Determine if the reference document is STRONGLY related to the question.
        - If the document is not STRONGLY related to the question, respond with just "I don't know" only, no other text.
        - If the document is STRONGLY related to the question, proceed to step 2.

    2. Generate a response directly answering the user's question using the context from the document. Focus only on the question, removing all irrelevant information.

    ---Guidelines---

    1. Provide answers to the question, supported by evidence or data from the document.

    2. Follow the structure:
        - Answer One: Description of the answer
        - Supporting Evidence: Specific details or DATA supporting the answer
        - Answer Two: Description of another relevant answer
        - Supporting Evidence: Specific details or DATA supporting the answer
        - (Continue this structure for all relevant answers identified in the document)

    3. Format the output for each answer as:

        answer1{{tuple_delimiter}}supporting evidence
        answer2{{tuple_delimiter}}supporting evidence
        answer3{{tuple_delimiter}}supporting evidence


    ---Input---
    Here is the Reference Document:

    {document}

    Here is the Question:

    {question}


    """
    answer = get_completion(prompt)

    return answer

@pandas_udf("string", PandasUDFType.SCALAR)
def ask_question(document_series):
  return document_series.apply(generate_response)

def aggregate(document, question):
    prompt = f"""

    ---Role---

    You are an advanced AI assistant tasked with creating comprehensive answers by integrating and expanding upon the partial insights provided by multiple analysts. 
    Each analyst has access to only a subset of the relevant documents or facts, resulting in incomplete individual conclusions.

    ---Guidelines---

    1. Synthesize these partial answers, identifying common threads and complementary information.
    2. Fill in gaps by inferring logical connections between the partial insights.
    3. Provide a broader, more complete perspective that goes beyond simply summarizing the analysts' views.
    4. Generate new insights or hypotheses based on the combined information.
    5. Highlight any potential inconsistencies or areas of uncertainty in the integrated view.
    6. Present a coherent, well-rounded answer that captures the full scope of the available information.
    
    ---Input---

    Here is the partial insights provided by multiple analysts:
    
    {document}
    
    Here is the Question: 
    
    {question}
    
    
    Now Please Response:

    """
    answer = get_completion(prompt)
    
    CONTINUE_PROMPT = """
  Expand your analysis. Consider overlooked perspectives and implications to provide a more comprehensive response:

  """
    new_prompt = prompt + '\n' + answer + '\n' + CONTINUE_PROMPT
    new_answer = get_completion(new_prompt)

    return new_answer


if __name__ == "__main__":
    api_token = os.getenv('Netmind_API_KEY')
    # Load the dataset
    dataset_path = 'elricwan/HarryPotter'
    dataset = load_dataset(dataset_path)
    sample_1 = dataset['train'][0]['content']
    documents = chunk_text_by_paragraph(sample_1)

    question = "This is from Harry Potter Book, now given the context, how many female character appeared in the context? please list all of them and remove duplicates."

    # Convert the list of documents to a PySpark DataFrame
    df = spark.createDataFrame([(text,) for text in documents], ["chunk"])
    # Use the ask_question function in parallel
    df_answers = df.withColumn("answer", ask_question(df["chunk"]))

    # save the answer to disk
    df_answers.write.mode("overwrite").json("jsonl/df_answers")

    # Read the JSON file into a DataFrame
    df_read = spark.read.json("jsonl/df_answers")

    # Collect all rows into a list
    rows = df_read.collect()
    points = []

    # Print the 'answer' column for each row
    for row in rows:
        if "don't know" not in row['answer']:
            points.append(row['answer'])

    Perspectives = ' '.join(points)
    final_answer = aggregate(Perspectives,question)
    print(final_answer)

    # End time
    end_time = time.time()

    # Execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

