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
def connect_to_milvus():
    uri = os.getenv('MILVUS_URI')
    token = os.getenv('MILVUS_TOKEN')
    connections.connect(uri=uri, token=token)
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

# Function to create collection for entities if not exists
def create_entity_collection_if_not_exists(collection_name: str):
    
    if collection_name in list_all_collections():
        print(f"Collection '{collection_name}' already exists.")
        delete_collection_if_exists(collection_name)

    fields = [
        FieldSchema(name="entity_id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="entity_name", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="entity_type", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="entity_description", dtype=DataType.VARCHAR, max_length=2048),
        FieldSchema(name="embedding_of_entity", dtype=DataType.FLOAT_VECTOR, dim=1024)
    ]
    schema = CollectionSchema(fields, description="collection for storing entities with embeddings")
    collection = Collection(name=collection_name, schema=schema)
    print(f"Collection '{collection_name}' created.")


# Function to create collection for relationships if not exists
def create_relationship_collection_if_not_exists(collection_name: str):
    if collection_name in list_all_collections():
        print(f"Collection '{collection_name}' already exists.")
        delete_collection_if_exists(collection_name)

    fields = [
        FieldSchema(name="relationship_id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="source_entity", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="target_entity", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="relationship_description", dtype=DataType.VARCHAR, max_length=2048),
        FieldSchema(name="embedding_of_relation", dtype=DataType.FLOAT_VECTOR, dim=1024)
    ]
    schema = CollectionSchema(fields, description="collection for storing relationships with embeddings")
    collection = Collection(name=collection_name, schema=schema)
    print(f"Collection '{collection_name}' created.")
   



# Function to insert entity data into collection
def insert_entity_data(collection_name: str, entities: List[Tuple[str, str, str, List[float]]]):
    collection = Collection(collection_name)
    entity_names = [entity[0] for entity in entities]
    entity_types = [entity[1] for entity in entities]
    entity_descriptions = [entity[2] for entity in entities]
    embeddings = [entity[3] for entity in entities]
    
    data = [
        entity_names,
        entity_types,
        entity_descriptions,
        embeddings
    ]
    collection.insert(data)
    print(f"Inserted {len(entities)} entities into collection '{collection_name}'")

# Function to insert relationship data into collection
def insert_relationship_data(collection_name: str, relationships: List[Tuple[str, str, str, List[float]]]):
    collection = Collection(collection_name)
    source_entities = [relation[0] for relation in relationships]
    target_entities = [relation[1] for relation in relationships]
    relationship_descriptions = [relation[2] for relation in relationships]
    embeddings = [relation[3] for relation in relationships]
    
    data = [
        source_entities,
        target_entities,
        relationship_descriptions,
        embeddings
    ]
    collection.insert(data)
    print(f"Inserted {len(relationships)} relationships into collection '{collection_name}'")

# Function to initialize and insert data into Milvus
def initialize_and_insert_data(entity_collection_name, relationship_collection_name, entities: List[Tuple[str, str, str, List[float]]], relationships: List[Tuple[str, str, str, List[float]]]):
    # Connect to Milvus
    connect_to_milvus()

    # Create collections if not exist
    create_entity_collection_if_not_exists(entity_collection_name)
    create_relationship_collection_if_not_exists(relationship_collection_name)

    # Insert data into collections
    insert_entity_data(entity_collection_name, entities)
    insert_relationship_data(relationship_collection_name, relationships)


def search_entity_by_embedding_and_type(collection_name: str, name_embedding: List[float], entity_type: str, top_k: int = 10):
    try:
        collection = Collection(collection_name)
        
        # Define search parameters
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        
        # Create an expression to filter by entity type
        expr = f"entity_type == '{entity_type}'"
        
        # Perform the search with the filter
        output_fields = ["entity_id", "entity_name", "entity_type", "entity_description"]  # Add the fields you want to retrieve
        results = collection.search(
            data=[name_embedding], 
            anns_field="embedding_of_entity", 
            param=search_params, 
            limit=top_k, 
            expr=expr,
            output_fields=output_fields
        )
        return results
    except Exception as e:
        print(f"An error occurred while searching entities: {e}")
        return None

def search_relationship_by_embedding(collection_name: str, relation_embedding: List[float], top_k: int = 10):
    try:
        collection = Collection(collection_name)
        
        # Define search parameters
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        
        # Perform the search
        output_fields = ["relationship_id", "source_entity", "target_entity", "relationship_description"]  # Add the fields you want to retrieve
        results = collection.search(
            data=[relation_embedding], 
            anns_field="embedding_of_relation", 
            param=search_params, 
            limit=top_k,
            output_fields=output_fields
        )
        return results
    except Exception as e:
        print(f"An error occurred while searching relationships: {e}")
        return None

    

if __name__ == "__main__":
    # Example usage
    # Define collection names
    entity_collection_name = "graphrag_entity_collection"
    relationship_collection_name = "graphrag_relationship_collection"

    entities = [
        ("entity1", "type1", "description1", [0.1] * 120),
        ("entity2", "type2", "description2", [0.2] * 120)
    ]

    relationships = [
        ("entity1", "entity2", "relationship1", [0.3] * 120),
        ("entity2", "entity1", "relationship2", [0.4] * 120)
    ]

    #initialize_and_insert_data(entity_collection_name, relationship_collection_name, entities, relationships)
    #connect_to_milvus()

    # Example search parameters
    # name_embedding = [0.1] * 120  # Example name embedding
    # entity_type = "type1"  # Example entity type

    # # Perform the search
    # collection_name = "entity_collection"
    # results = search_entity_by_embedding_and_type(collection_name, name_embedding, entity_type)

    # # Print the results
    # for result in results:
    #     print(f"Entity ID: {result.id}")
    #     print(f"Entity Name: {result.entity_name}")
    #     print(f"Entity Type: {result.entity_type}")
    #     print(f"Entity Description: {result.entity_description}")
    #     print("-" * 50)
