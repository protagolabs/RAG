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

    You are a helpful assistant responding to a question based on the provided paragraph.

    ---Goal---

    1. Determine if the given document is related to the user's query.
        - If the document is not related to the query, respond with "I don't know."
        - If the document is related to the query, proceed to step 2.

    2. Generate a response directly answering the user's question using the context from the document. Focus only on the question, removing all irrelevant information.

    ---Guidelines---

    1. Provide answers to the user's query, supported by evidence or data from the document.

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
    

    ######################   
    ---Example---
    ###################### 
    Here is the Document: 

    "The solar system consists of the Sun and the objects that orbit it, including eight planets, their moons, and other celestial bodies such as asteroids and comets. The Sun, which is a star, contains 99.86% of the solar system's mass. The four inner planets, Mercury, Venus, Earth, and Mars, are rocky, while the outer planets, Jupiter, Saturn, Uranus, and Neptune, are gas giants except for Neptune and Uranus, which are ice giants. The asteroid belt, which lies between Mars and Jupiter, contains many small rocky bodies. "
    
    Here is the Question: 

    "What are the main components of the solar system?"
    
    ###################### 
    Output:

    the Sun and the objects that orbit it {{tuple_delimiter}} The solar system consists of the Sun and the objects that orbit it, including eight planets, their moons, and other celestial bodies such as asteroids and comets.
    The Planets {{tuple_delimiter}} The eight planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.
    The Asteroid Belt {{tuple_delimiter}} The asteroid belt, which lies between Mars and Jupiter, contains many small rocky bodies. 

    
    ---Input---
    Here is the document: 
    
    {document}

    Here is the question:

    {question}
    
    Now Please Respond:
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

    #return results


if __name__ == "__main__":
    # generate raw answers
    input_file = '../chunk/output.jsonl'
    output_file = 'jsonl/raw_answers.jsonl'  
    question = "What is the current state of autonomous vehicles?"  

    map_reduce_documents(input_file, output_file, question)
