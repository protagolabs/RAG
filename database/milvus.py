from pymilvus import (
    connections,
    db,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
    utility
)
from typing import List, Dict
from dotenv import load_dotenv
import os
import uuid

# Load environment variables
load_dotenv()

def generate_uuid():
    return uuid.uuid4().int & (1<<63) - 1

# Function to connect to Milvus
def connect_to_milvus(uri: str, token: str):
    connections.connect(uri=uri, token=token)
    print("Connected to Milvus")

# Function to list all databases
def list_databases():
    return db.list_database()

# Function to list all collections
def list_all_collections():
    return utility.list_collections()

def create_collection_with_metadata(collection_name: str):
    fields = [
        FieldSchema(name="global_unique_id", dtype=DataType.INT64, is_primary=True, auto_id=False),
        FieldSchema(name="user_id", dtype=DataType.INT64),
        FieldSchema(name="timestamp", dtype=DataType.INT64),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=120)
    ]
    schema = CollectionSchema(fields, description="example collection with user metadata")
    collection = Collection(name=collection_name, schema=schema)
    return collection
    
# Function to insert data with metadata into a collection
def insert_data_with_metadata(collection_name: str, vectors: List[List[float]], global_unique_id: List[int], user_ids: List[int], timestamps: List[int]):
    collection = Collection(collection_name)
    data = [
        global_unique_id,  
        user_ids,
        timestamps,
        vectors
    ]
    collection.insert(data)
    print(f"Inserted {len(vectors)} vectors with metadata into collection '{collection_name}'")

# Function to create an index for a collection
def create_index(collection_name: str):
    collection = Collection(collection_name)
    index_params = {
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128},
        "metric_type": "L2"
    }
    collection.create_index(field_name="vector", index_params=index_params)
    collection.load()
    print(f"Index created and collection '{collection_name}' loaded")


# Function to update data in a collection
def update_data(collection_name: str, ids: List[int], new_vectors: List[List[float]]):
    collection = Collection(collection_name)
    collection.delete(ids)
    data = [
        ids,
        new_vectors
    ]
    collection.insert(data)
    collection.load()
    print(f"Updated data in collection '{collection_name}'")

# Function to read data from a collection
def read_data(collection_name: str, ids: List[int]):
    collection = Collection(collection_name)
    results = collection.query(expr=f"id in {ids}")
    return results

# Function to delete data from a collection
def delete_data(collection_name: str, ids: List[int]):
    collection = Collection(collection_name)
    collection.delete(ids)
    collection.load()
    print(f"Deleted data from collection '{collection_name}'")

# Function to perform a search in a collection based on vector and metadata
def search_collection(collection_name: str, query_vectors: List[List[float]], top_k: int = 10, user_id_max: int = None, timestamp_range: tuple = None):
    collection = Collection(collection_name)
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    
    # Create an expression for filtering based on metadata conditions
    expr_parts = []
    if user_id_max is not None:
        expr_parts.append(f"user_id < {user_id_max}")
    if timestamp_range is not None and len(timestamp_range) == 2:
        expr_parts.append(f"timestamp >= {timestamp_range[0]} and timestamp <= {timestamp_range[1]}")
    
    expr = " and ".join(expr_parts) if expr_parts else None
    
    # Perform the search with the metadata filter
    output_fields = ["global_unique_id", "user_id", "timestamp"]  # Add the fields you want to retrieve
    results = collection.search(
        query_vectors, 
        "vector", 
        search_params, 
        limit=top_k, 
        expr=expr,
        output_fields=output_fields
    )
    
    return results

# Function to list all collections
def list_collections():
    return utility.list_collections()

# Function to drop a collection
def drop_collection(collection_name: str):
    utility.drop_collection(collection_name)
    print(f"Dropped collection '{collection_name}'")

# Sample usage
if __name__ == "__main__":
    uri = os.getenv('MILVUS_URI')
    token = os.getenv('MILVUS_TOKEN')
    MILVUS_COLLECTION = os.getenv('MILVUS_COLLECTION')

    # Connect to Milvus
    connect_to_milvus(uri, token)

    # List all databases
    databases = list_databases()
    print("Databases:", databases)

    # List all collections
    collections = list_all_collections()
    print("Collections:", collections)

    # # Create a new collection
    collection_name = MILVUS_COLLECTION

    # Drop collection if it exists
    if utility.has_collection(collection_name):
        utility.drop_collection(collection_name)
    print(f"Existing collection '{collection_name}' dropped.")

    # create new collection
    collection = create_collection_with_metadata(collection_name)
    print(f"Created collection '{collection_name}'")

    

    # Insert sample data with metadata into the collection
    sample_vectors = [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] * 12] * 5
    sample_global_unique_id = [generate_uuid() for _ in range(5)]
    sample_user_ids = [101, 102, 103, 104, 105]
    sample_timestamps = [1627890123, 1627891123, 1627892123, 1627893123, 1627894123]
    insert_data_with_metadata(collection_name, sample_vectors, sample_global_unique_id, sample_user_ids, sample_timestamps)
    create_index(collection_name)


    # search a vector
    query_vectors = [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] * 12]
    
    
    # Define metadata conditions
    user_id_max = 1000  # Example condition: user_id less than 1000
    timestamp_range = (1527890123, 1727890123)  # Example condition: timestamp between 1527890123 and 1727890123
    

    search_results = search_collection(collection_name, query_vectors, top_k=10, user_id_max=user_id_max, timestamp_range=timestamp_range)
    for result in search_results:
        print(result)


    
