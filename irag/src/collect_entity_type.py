import json
import jsonlines
from openai import OpenAI
import torch
import ollama
import re
from datasets import load_dataset

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

def get_type(question):
    prompt = f"""

    ---Role---
    You are an expert in natural language processing tasked with identifying relevant entity types for each question.

    ---Goal---
    Analyze the provided questions and identify the entity types that best represent the information being asked for. The output should include the entity type and a brief description of what the entity type refers to, using the specified format.

    Format entity type
    <entity_type>{{tuple_delimiter}}<entity_type_description>
    <entity_type>{{tuple_delimiter}}<entity_type_description>
    <entity_type>{{tuple_delimiter}}<entity_type_description>

    DO NOT OUTPUT ANY OTHER TEXT.

    ---Examples--- 
    ######################
    Questions:

    what is tosca automation tool
    meaning of addae in african
    what is compressed air
    most important battle of world war 2
    what is the theme song
    what eats a bat
    what uses real time os
    what is transient global am
    what is mechanical handling equipment
    what is the lcd math
    what is the definition of sympathy
    ariat international inc return address
    what is the perimeter of triangle
    how long to keep cpe records
    definition of capias issued on a background
    what is the bovine growth hormone
    what is a phosphodiesterase inhibitor
    samsung galaxy s6 edge att price
    modality cardinal meaning
    How to make a cake
    ######################
    Output:

    Definition{{tuple_delimiter}}Explanations or interpretations of terms, concepts, and legal aspects.
    Event{{tuple_delimiter}}Significant occurrences or happenings, often historical.
    Media{{tuple_delimiter}}Creative works such as songs, films, books, etc.
    Biology{{tuple_delimiter}}The study of living organisms, including animals and plants.
    Technology{{tuple_delimiter}}The application of scientific knowledge for practical purposes, especially in industry.
    Health{{tuple_delimiter}}Aspects related to physical or mental well-being.
    Business{{tuple_delimiter}}Information related to companies, commerce, or finance.
    Mathematics{{tuple_delimiter}}The abstract science of number, quantity, and space.
    Product{{tuple_delimiter}}An item or service available for sale.
    Action{{tuple_delimiter}}Specific activities, behaviors, or processes, including methods or procedures.


    ---Input---

    Questions: 
    
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

def process_from_datasets(output_file):
    # load dataset
    passages = load_dataset("UKPLab/dapr", "MSMARCO-corpus", split="test")
    queries = load_dataset("UKPLab/dapr", "MSMARCO-queries", split="test")
    qrels_rows = load_dataset("UKPLab/dapr", "MSMARCO-qrels", split="test")

    # generate entity type
    idx = 0
    question = ''
    with jsonlines.open(output_file, mode='w') as writer:
        for query in queries:
            if idx > 10:
                idx = 0
                answer = get_type(question)
                question = ''
                result = {'answer':answer}
                writer.write(result)
            else:
                idx += 1
                question += query['text'] + '\n'
        answer = get_type(question)
        result = {'answer':answer}
        writer.write(result)



if __name__ == "__main__": 

    output_file = 'jsonl/entity_type.jsonl'
    process_from_datasets(output_file)
