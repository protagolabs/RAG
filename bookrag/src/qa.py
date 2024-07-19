import json
import jsonlines
from openai import OpenAI
import torch
import ollama
import re

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

def ask_question(document, question):
    prompt = f"""

    ---Role---

    You are a helpful assistant responding to a question based on provided paragraph.

    ---Goal---

    Generate a response consisting of a list of key points that responds to the user's question, you should remove all irrelevant information, only focus on the question. If the question is not answerable, respond with "I don't know."
    If the document cannot be used to answer the question, respond with "I don't know.".
    
    Each key point in the response should have the following element:
    - Description: A comprehensive description of the point.
    - Importance Score: An integer score between 0-100 that indicates how important the point is in answering the user's question. An 'I don't know' type of response should have a score of 0.

    The response should be JSON formatted enclosed in Markdown code blocks tagged with 'json'. For example:
    
    ```json
    {{
        "points": [
            {{"description": "Description of point 1 [Data: Reports (report ids)]", "score": score_value}},
            {{"description": "Description of point 2 [Data: Reports (report ids)]", "score": score_value}}
        ]
    }}
    ```
    
    ---Guidelines--- 

    Document-Based Answer Only: Use only the information contained within the provided document to answer the question. Do not include any external knowledge or information that is not found in the document.

    Direct Quotes and Original Phrasing: Whenever possible, use the exact sentences, phrases, or words from the document. Your answer should closely reflect the language and terminology used in the document.

    No Answer Provided: If the document does not contain the information needed to answer the question, respond with "I don't know." Do not attempt to answer the question based on your own knowledge or assumptions.

    ---Input---

    Here is the Document: 
    
    {document}
    
    Here is the Question: 
    
    {question}
    
    
    Now Please Answer:

    """
    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": prompt}],
        max_tokens=2000,
        n=1,
        temperature=0.1,
    )
    answer = response.choices[0].message.content
    
    return answer

def map_reduce_documents(input_file, output_file, question):
    # Read the input JSONL file
    with jsonlines.open(input_file, mode='r') as reader:
        documents = [doc for doc in reader]
    
    # Map step: ask the question to each document
    results = []
    for doc in documents:
        for key, value in doc.items():
            # Assuming the document text is the value of the key
            document_text = value
            answer = ask_question(document_text, question)
            try:
                answer = extract_dict_from_json(answer)
                answer = json.loads(answer)
                results.append({'doc_id': key, 'points': answer['points']})
            except:
                pass
            
    # Reduce step: write the results to the output JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        for result in results:
            writer.write(result)

    #return results

def extract_dict_from_json(text: str):
        """
        Extract the dictionary between "```json" and "```". 
        """
        pattern = r'```json(.*?)```'
        extracted_text = re.findall(pattern, text, re.DOTALL)

        return extracted_text[0].strip() 

if __name__ == "__main__":
    # generate raw answers
    input_file = '../chunk/output.jsonl'
    output_file = 'jsonl/raw_answers.jsonl'  
    question = "What is the current state of autonomous vehicles?"  

    map_reduce_documents(input_file, output_file, question)
