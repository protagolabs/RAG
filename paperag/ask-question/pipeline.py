import json
import jsonlines
import numpy as np
from openai import OpenAI
import torch
import ollama
import re
import igraph as ig
import leidenalg as la
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the Ollama LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

# collect raw answers
def ask_question(document, question):
    prompt = f"""

    ---Role---

    You are a helpful assistant responding to a question based on provided paragraph.

    ---Goal---

    Generate a response consisting of a list of key points that responds to the user's question, summarizing all relevant information from the provided paragraph.
    
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

def extract_dict_from_json(text: str):
        """
        Extract the dictionary between "```json" and "```". 
        """
        pattern = r'```json(.*?)```'
        extracted_text = re.findall(pattern, text, re.DOTALL)

        return extracted_text[0].strip() 

# filter raw answers
def filter_answer(input_file, output_file, score_threshold=80):
    # Read JSONL file using jsonlines
    with jsonlines.open(input_file, mode='r') as reader:
        data = [doc for doc in reader]

    # Collect all points globally
    all_points = []
    for entry in data:
        for point in entry['points']:
            if point['score'] >= score_threshold:
                all_points.append({"doc_id": entry['doc_id'], "description": point['description'], "score": point['score']})

    # Sort the points globally based on score
    all_points.sort(key=lambda x: x['score'], reverse=True)

    # Write the processed data to a new JSONL file using jsonlines
    with jsonlines.open(output_file, mode='w') as writer:
        for entry in all_points:
            writer.write(entry)

    print(f"Filtered and globally ranked data saved to {output_file}")

    return all_points

# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding

# clustering answers
def leiden_cluster_points(points, output_file, resolution_parameter=1.4):

    # Calculate embeddings for all points
    embeddings = np.array([calculate_embedding(point) for point in points])

    # Construct similarity graph using cosine similarity
    similarity_matrix = cosine_similarity(embeddings)
    np.fill_diagonal(similarity_matrix, 0)  # Remove self-similarity
    edges = np.argwhere(similarity_matrix > 0)
    weights = similarity_matrix[edges[:, 0], edges[:, 1]]

    # Create igraph graph
    g = ig.Graph()
    g.add_vertices(len(points))
    g.add_edges(edges)
    g.es['weight'] = weights

    # Apply Leiden Algorithm
    partition = la.find_partition(g, la.CPMVertexPartition, weights='weight', resolution_parameter=resolution_parameter)

    # Organize points by cluster labels
    clusters = {}
    for idx, cluster_id in enumerate(partition.membership):
        if cluster_id not in clusters:
            clusters[cluster_id] = []
        clusters[cluster_id].append(points[idx])

    # Save clusters to a JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        for label, points in clusters.items():
            writer.write({str(label): points})

    print(f"Clusters saved to {output_file}")

# aggregate answers
def aggregate(document, question):
    prompt = f"""

    ---Role---

    You are a helpful assistant responding to questions about a dataset by synthesizing perspectives from multiple analysts.

    ---Goal---

    Generate a response of the target length and format that responds to the user's question, summarize all the reports from multiple analysts.
    
    - Description: A comprehensive response summarized from multiple analysts.
   
    
    ---Guidelines--- 

    The final response should remove all irrelevant information from the analysts' reports and merge the cleaned information into a comprehensive answer that provides explanations of all the key points and implications.

    No Answer Provided: If you think the dataset is irrelevant or not suitable to the question, respond with "I don't know." Do not attempt to answer the question based on your own knowledge or assumptions.

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
    
    return answer

def process_aggregate(input_file, output_file, question):
    # Read the input JSONL file
    with jsonlines.open(input_file, mode='r') as reader:
        documents = [doc for doc in reader]

    # Map step: ask the question to each document
    results = []
    for doc in documents:
        for key, value in doc.items():
            # Assuming the document text is the value of the key
            document_text = '\n\n'.join(value)
            answer = aggregate(document_text, question)
            # Filter out "I don't know" from the answer
            if "don't know" not in answer:
                results.append({key: answer})

    # Save the answers to a new JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        writer.write_all(results)

    print(f"Answers saved to {output_file}")


if __name__ == "__main__":
    # generate raw answers
    input_file = '../chunk/output.jsonl'
    output_file = 'jsonl/raw_answers.jsonl'  
    question = "What is the current state of autonomous vehicles?"  

    map_reduce_documents(input_file, output_file, question)

    print(f"Answers saved to {output_file}")

    # filter raw answers
    input_file = 'jsonl/raw_answers.jsonl'
    output_file = 'jsonl/filter_answers.jsonl'
    all_points = filter_answer(input_file, output_file)

    # clustering
    # Sample list of points
    points = [all_point["description"] for all_point in all_points] 
    output_file = 'jsonl/cluster_points.jsonl'
    leiden_cluster_points(points, output_file)

    # aggregate
    input_file = 'jsonl/cluster_points.jsonl'
    output_file = 'jsonl/aggregate_answers.jsonl'
    process_aggregate(input_file, output_file, question)

