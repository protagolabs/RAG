from datasets import load_dataset
import ollama
import numpy as np
import json
from src.milvus_database import connect_to_milvus, create_index, search_document_by_embedding

document_collection_name = "graphrag_document_collection"
connect_to_milvus()


# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding


# passages = load_dataset("UKPLab/dapr", "MSMARCO-corpus", split="test")
# queries = load_dataset("UKPLab/dapr", "MSMARCO-queries", split="test")
# qrels_rows = load_dataset("UKPLab/dapr", "MSMARCO-qrels", split="test")

role_answer = load_dataset("elricwan/MSMARCO-queries-roleAns", split="train")

retrieve = {}
for role_ in role_answer:
    _id = role_["_id"]
    tmp = []
    seen_ids = set()
    answers = role_["answers"]
    question = role_["text"]

    # use question to find reference
    embedding = calculate_embedding(question)
    document_results = search_document_by_embedding(document_collection_name, embedding, 30)
    document_results = document_results[0]
    for result in document_results:
        if result.id not in seen_ids:
            tmp.append((result.id,result.distance))
            seen_ids.add(result.id)

    # use answer to find reference
    for key in answers:
        ans = answers[key]
        if 'do not know' not in ans:
            embedding = calculate_embedding(ans)
            document_results = search_document_by_embedding(document_collection_name, embedding, 30)
            document_results = document_results[0]
            for result in document_results:
                if result.id not in seen_ids:
                    tmp.append((result.id,result.distance))
                    seen_ids.add(result.id)
        
    retrieve[_id] = tmp

with open('jsonl/data.json', 'w') as json_file:
    json.dump(retrieve, json_file, indent=4)
print("Data saved to data.json")