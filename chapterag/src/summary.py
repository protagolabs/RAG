import json
import jsonlines
from openai import OpenAI
from collections import defaultdict
import copy
import torch
import ollama

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

def summarize_text(document, max_tokens=500):
    prompt = f"""
    ---Role---
    You are an expert summarizer with a deep understanding of hierarchical argument structures.

    ---Goal---
    Your task is to summarize the provided document by identifying the main arguments and supporting them with specific details or data, using the Hierarchical Argument Summarization Method. Ensure the summary is refined and retains all crucial information.

    ---Guidelines--- 
    1. Identify the main arguments in the document.
    
    2. For each main argument, provide supporting evidence or data.
    
    3. Follow the structure: 
        - Main Argument One: Description of the primary argument
          - Supporting Evidence: Specific details or DATA supporting the argument
        - Main Argument Two: Description of another primary argument
          - Supporting Evidence: Specific details or DATA supporting the argument
        - (Continue this structure for all main arguments identified in the document)
        Note: Supporting Evidence should be specific and relevant to the main argument, providing context or data to support the claim. 
    
    4. Format the output for each argument as:
       argument1{{tuple_delimiter}}supporting evidence
       argument2{{tuple_delimiter}}supporting evidence
       argument3{{tuple_delimiter}}supporting evidence
    
    5. When finished, output {{completion_delimiter}}

    ######################   
    ---Example---
    ###################### 
    Text:
    "XYZ Company launched a new product in July 2023. This launch was successful due to innovative research and effective marketing strategies. Market research prior to the launch indicated a strong demand for the product, and the product's features met user expectations. Post-launch, the product achieved ten thousand monthly active users, and user feedback was overwhelmingly positive, indicating high satisfaction rates."
    ###################### 
    Output:

    XYZ Company successfully launched a new product {{tuple_delimiter}} The product was launched globally in July 2023. The success was achieved through innovative research and effective marketing.
    The new product meets market demands" {{tuple_delimiter}} Market research indicated a strong demand for the product. The product's features and functionalities met user expectations.
    The new product performs well in the market" {{tuple_delimiter}} The product achieved ten thousand monthly active users. User feedback was positive, with high satisfaction rates.

    {{completion_delimiter}}
    
    ---Input---
    Here is the document: 
    
    {document}
    
    Now Please Respond:
"""

    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": prompt}],
        max_tokens=max_tokens,
        n=1,
        temperature=0.1,
    )
    answer = response.choices[0].message.content
    
    return answer


def process_summarize(input_file, output_file):
    # Read the input JSONL file
    with jsonlines.open(input_file, mode='r') as reader:
        documents = [doc for doc in reader]
    
    # summarize text
    results = []
    for doc in documents:
        doc_id, document_text, filename = doc.values()
        answer = summarize_text(document_text)
        results.append({'doc_id': doc_id,'filename': filename, 'summary': answer})
    
    # Reduce step: write the results to the output JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        for result in results:
            writer.write(result)