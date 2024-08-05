from datasets import load_dataset
from .milvus_database import connect_to_milvus, create_document_collection_if_not_exists, insert_document_data, create_index
import ollama
import numpy as np
# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding

# save embeddings to milvus
document_collection_name = "graphrag_document_collection"

def save_embedding_to_milvus(document_collection_name):
    
    passages = load_dataset("UKPLab/dapr", "MSMARCO-corpus", split="test")
    passages = passages.select(range(1000000))
    #passages = passages.select(range(10))

    documents = []
    batch_size = 1000

    connect_to_milvus()
    create_document_collection_if_not_exists(document_collection_name)

    for passage in passages:
        _id = passage['_id']
        text = passage['text']
        doc_id = passage['doc_id']
        embedding = calculate_embedding(text)
        documents.append((_id, doc_id, embedding))

        # Insert documents in batches of 1000
        if len(documents) == batch_size:
            insert_document_data(document_collection_name, documents)
            documents = []

    
    
    # Insert any remaining documents
    if documents:
        insert_document_data(document_collection_name, documents)
    #create_index(document_collection_name, "text_embedding")