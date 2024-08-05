from pymilvus import (
    connections,
    db,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
    utility
)
from typing import List, Tuple
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# uri = os.getenv('MILVUS_URI')
# token = os.getenv('MILVUS_TOKEN')
# MILVUS_COLLECTION = os.getenv('MILVUS_COLLECTION')

# Function to connect to Milvus
# def connect_to_milvus():
#     uri = os.getenv('MILVUS_URI')
#     token = os.getenv('MILVUS_TOKEN')
#     connections.connect(uri=uri, token=token)
#     print("Connected to Milvus")
def connect_to_milvus():
    alias = "default"
    host = os.getenv('MILVUS_host')
    port='19530'
    connections.connect(
        alias=alias, 
        host=host,
        port=port
    )
    print("Connected to Milvus")

# Function to list all collections
def list_all_collections():
    return utility.list_collections()

def delete_collection_if_exists(collection_name: str):
    if collection_name in list_all_collections():
        collection = Collection(name=collection_name)
        collection.drop()
        print(f"Collection '{collection_name}' deleted.")
    else:
        print(f"Collection '{collection_name}' does not exist.")

# Function to create collection for documents if not exists
def create_document_collection_if_not_exists(collection_name: str):
    if collection_name in list_all_collections():
        print(f"Collection '{collection_name}' already exists.")
        delete_collection_if_exists(collection_name)

    fields = [
        FieldSchema(name="_id", dtype=DataType.VARCHAR, max_length=255, is_primary=True),
        FieldSchema(name="doc_id", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="text_embedding", dtype=DataType.FLOAT_VECTOR, dim=1024)
    ]
    schema = CollectionSchema(fields, description="collection for storing documents with text embeddings")
    collection = Collection(name=collection_name, schema=schema)
    print(f"Collection '{collection_name}' created.")


# Function to insert document data into collection
def insert_document_data(collection_name: str, documents: List[Tuple[str, str, List[float]]]):
    collection = Collection(collection_name)
    ids = [doc[0] for doc in documents]
    doc_ids = [doc[1] for doc in documents]
    embeddings = [doc[2] for doc in documents]
    
    data = [
        ids,
        doc_ids,
        embeddings
    ]
    collection.insert(data)
    print(f"Inserted {len(documents)} documents into collection '{collection_name}'")


# Function to create an index for a collection
def create_index(collection_name: str, field_name: str):
    try:
        collection = Collection(collection_name)
        index_params = {
            "index_type": "IVF_FLAT",
            "params": {"nlist": 32},  # Number of clusters
            "metric_type": "L2"  # Distance metric: Euclidean distance
        }
        collection.create_index(field_name=field_name, index_params=index_params)
        collection.load()
        print(f"Index created and collection '{collection_name}' loaded")
    except Exception as e:
        print(f"An error occurred while creating index for collection '{collection_name}': {e}")


def search_document_by_embedding(collection_name: str, text_embedding: List[float], top_k: int = 10):
    try:
        collection = Collection(collection_name)
        
        # Define search parameters
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        
        # Perform the search
        output_fields = ["_id", "doc_id"]  # Add the fields you want to retrieve
        results = collection.search(
            data=[text_embedding], 
            anns_field="text_embedding", 
            param=search_params, 
            limit=top_k,
            output_fields=output_fields
        )
        return results
    except Exception as e:
        print(f"An error occurred while searching documents: {e}")
        return None

def search_document_by_id(collection_name: str, document_id: str):
    try:
        collection = Collection(collection_name)
        
        # Create an expression to filter by _id
        expr = f"_id == '{document_id}'"
        
        # Perform the search with the filter
        output_fields = ["_id", "doc_id", "text_embedding"]  # Add the fields you want to retrieve
        results = collection.query(
            expr=expr,
            output_fields=output_fields
        )
        return results
    except Exception as e:
        print(f"An error occurred while searching for document by _id: {e}")
        return None


if __name__ == "__main__":
    # Define collection names
    document_collection_name = "graphrag_document_collection"

    documents = [
        ("D2147834-0", "D2147834", [0.5] * 1024),
        ("D2147835-0", "D2147835", [0.6] * 1024)
    ]

    connect_to_milvus()
    create_document_collection_if_not_exists(document_collection_name)
    insert_document_data(document_collection_name, documents)
    create_index(document_collection_name, "text_embedding")

    # Example search parameters
    search_embedding = [0.5] * 1024  # Example name embedding
    document_results = search_document_by_embedding(document_collection_name, search_embedding)
    for result in document_results:
        print(result)

    # Example search by _id
    document_id = "D2147834-0"
    document_by_id = search_document_by_id(document_collection_name, document_id)
    #print(document_by_id)
