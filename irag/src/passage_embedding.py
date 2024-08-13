from datasets import load_dataset
from .milvus_database import connect_to_milvus, create_document_collection_if_not_exists, insert_document_data, create_index
import ollama
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding

# Function to calculate embeddings for a batch of passages
def calculate_embeddings_batch(passages_batch):
    return [(passage['_id'], passage['doc_id'], calculate_embedding(passage['text'])) for passage in passages_batch]

# save embeddings to milvus
document_collection_name = "graphrag_document_collection"

def save_embedding_to_milvus(document_collection_name):
    
    passages = load_dataset("UKPLab/dapr", "MSMARCO-corpus", split="test")
    #passages = passages.select(range(1000000))
    #passages = passages.select(range(10))
    passages = passages.select(range(2540020, len(passages)))
    total_rows = len(passages)

    documents = []
    batch_size = 1000
    num_workers = 10  # Adjust this based on your GPU utilization and memory
    insert_batch_size = batch_size * num_workers  # Total insert batch size (5000)

    connect_to_milvus()
    #create_document_collection_if_not_exists(document_collection_name)

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
    
    # with ThreadPoolExecutor(max_workers=num_workers) as executor:
    #     futures = []
    #     for i in range(0, len(passages), batch_size):
    #         batch = passages.select(range(i, min(i + batch_size, total_rows)))
    #         # Convert the batch to a pandas DataFrame and then to a list of dictionaries
    #         batch = batch.to_pandas().to_dict(orient='records')
    
    #         futures.append(executor.submit(calculate_embeddings_batch, batch))
            
        
    #     for future in as_completed(futures):
    #         documents.extend(future.result())
    #         # Insert documents in batches of 5000
    #         while len(documents) >= insert_batch_size:
    #             insert_document_data(document_collection_name, documents[:insert_batch_size])
    #             documents = documents[insert_batch_size:]

    # # Insert any remaining documents
    # if documents:
    #     insert_document_data(document_collection_name, documents)
    
    
    create_index(document_collection_name, "text_embedding")