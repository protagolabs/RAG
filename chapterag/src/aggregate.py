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

def aggregate(document, question):
    prompt = f"""

    ---Role---

    You are a helpful assistant responding to questions about a dataset by synthesizing perspectives from multiple analysts.

    ---Goal---

    Generate a response of the target length and format that responds to the user's question, merge all the perspectives from multiple analysts.
    
    - Description: A comprehensive response summarized from multiple analysts.
   
    
    ---Guidelines--- 

    The final response should remove all irrelevant information from the analysts' perspectives and merge the cleaned information into a comprehensive answer that provides explanations of all the key points and implications.

    ---Input---

    Here is the Dataset: 
    
    {document}
    
    Here is the Question: 
    
    {question}
    
    
    Now Please Response:

    """
    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": prompt}],
        max_tokens=2000,
        n=1,
        temperature=0.1,
    )
    answer = response.choices[0].message.content
    
    CONTINUE_PROMPT = """
    MANY perspectives were missed in last synthesizing. Include them to generate a comprehensive response:
    
    """
    new_prompt = prompt + '\n' + answer + '\n' + CONTINUE_PROMPT
    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": new_prompt}],
        max_tokens=2000,
        n=1,
        temperature=0.1,
    )
    new_answer = response.choices[0].message.content

    return new_answer

def process_aggregate(input_file, output_file, question):
    # Read the input JSONL file
    with jsonlines.open(input_file, mode='r') as reader:
        documents = [doc for doc in reader]

    results = []
    reference_doc = []
    document_text = ""
    for doc in documents:
        doc_id, file_name, answer, reference, question = doc.values()
        if "don't know" not in answer:
            document_text += answer + "\n\n"
            for line in answer.split('\n'):
                if len(line) > 50:
                    reference_doc.append({doc_id: doc_id, 'file_name': file_name, 'reference': line, 'question': question})
    
    answer = aggregate(document_text, question)
    results.append({question: answer})

    # Save the answers to a new JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        writer.write_all(results)
    with jsonlines.open('jsonl/reference_doc.jsonl', mode='w') as writer:
        writer.write_all(reference_doc)

    print(f"Answers saved to {output_file}")

if __name__ == "__main__":

    input_file = 'jsonl/hierarchical_cluster_result.jsonl'  # Replace with your input file path
    output_file = 'jsonl/output.jsonl'  # Replace with your desired output file path
    question = "What is the current state of autonomous vehicles?"  # Replace with your actual question
    process_aggregate(input_file, output_file, question)


# target_level = 1
# level_key_prefix = f"level_{target_level}_community_"

# # Read the input JSONL file
# with jsonlines.open(input_file, mode='r') as reader:
#     documents = [
#         {key: value}
#         for doc in reader
#         for key, value in doc.items()
#         if key.startswith(level_key_prefix)
#     ]

# # Map step: ask the question to each document
# results = []
# for doc in documents:
#     for key, value in doc.items():
#         # Assuming the document text is the value of the key
#         document_text = '\n'.join(value)
#         answer = aggregate(document_text, question)
#         # Filter out "I don't know" from the answer
#         if "don't know" not in answer:
#             results.append({key: answer})

# # Save the answers to a new JSONL file
# with jsonlines.open(output_file, mode='w') as writer:
#     writer.write_all(results)

# print(f"Answers saved to {output_file}")