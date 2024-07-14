import json
import jsonlines
from openai import OpenAI
import torch
import ollama

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

def ask_question(document, question):
    prompt = f"""

    You will be provided with a document and a specific question. Your task is to answer the question strictly based on the content of the given document. Follow these guidelines when formulating your answer:

    Document-Based Answer Only: Use only the information contained within the provided document to answer the question. Do not include any external knowledge or information that is not found in the document.

    Direct Quotes and Original Phrasing: Whenever possible, use the exact sentences, phrases, or words from the document. Your answer should closely reflect the language and terminology used in the document.

    Focus on Arguments, Definitions, Points, and Evidence: Ensure that your answer highlights the key arguments, definitions, points, or pieces of evidence as they are presented in the document. Do not infer or interpret beyond what is explicitly stated.

    No Answer Provided: If the document does not contain the information needed to answer the question, respond with "No answer provided." Do not attempt to answer the question based on your own knowledge or assumptions.

    Example:

    Document: "The quick brown fox jumps over the lazy dog. The fox is known for its agility and speed, often outmaneuvering its predators."

    Question: "What characteristics are attributed to the fox in the document?"

    Answer: "The fox is known for its agility and speed."

    Document: "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll."

    Question: "What is photosynthesis?"

    Answer: "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll."

    Document: "Quantum mechanics is a fundamental theory in physics."

    Question: "Who developed quantum mechanics?"

    Answer: "No answer provided."

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
            results.append({'doc_id': key, 'answer': answer})
    
    # Reduce step: write the results to the output JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        for result in results:
            writer.write(result)

# Example usage
input_file = '../chunk/output.jsonl'
output_file = 'output_answers.jsonl'
question = "what is the current state of autonomous vehicles? What is the Potential impact of autonomous vehicles on urban mobility and city design "

map_reduce_documents(input_file, output_file, question)
