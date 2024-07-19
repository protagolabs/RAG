import json
import jsonlines
from openai import OpenAI
import torch
import ollama
import numpy as np
import re
import igraph as ig
import leidenalg as la
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter, defaultdict


# Define the tuple delimiter used in the input
tuple_delimiter = "{tuple_delimiter}"

def standardize_delimiter(input_string, standard_delimiter="{tuple_delimiter}"):
    # Define the regex pattern to match any case variation of {tuple_delimiter}
    pattern = re.compile(r'\{tuple_delimiter\}', re.IGNORECASE)
    
    # Replace all variations with the standard delimiter
    standardized_string = pattern.sub(standard_delimiter, input_string)
    
    return standardized_string

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

# Function to read the JSONL file
def read_jsonl(file_path):
    with jsonlines.open(file_path, mode='r') as reader:
        return [doc for doc in reader]

# Helper function to write JSONL file
def write_jsonl(file_path, data):
    with jsonlines.open(file_path, mode='w') as writer:
        writer.write_all(data)

# Function to parse the input data
def parse_input(data):
    entities = []
    relationships = []

    for record in data:
        lines = record['entity'].split('\n')
        for line in lines:
            line = standardize_delimiter(line)
            parts = line.split(tuple_delimiter)
            if parts[0].strip('"') == "entity":
                entities.append((parts[1], parts[2], parts[3], record['document'], record['doc_id'], record['filename']))
            elif parts[0].strip('"') == "relationship":
                relationships.append((parts[1], parts[2], parts[3], int(parts[4]), record['document'], record['doc_id'], record['filename']))
                
    return entities, relationships

# remove duplicated based on name and type
def remove_duplicates(tuples_list):
    unique_items = {}
    for item in tuples_list:
        name = item[0]
        if name not in unique_items:
            unique_items[name] = item
    return list(unique_items.values())

# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding

# in each group, find the most common name as the entity name
def most_common_or_first(my_list):
    if not my_list:
        return None
    
    counter = Counter(my_list)
    most_common = counter.most_common(1)
    
    return most_common[0][0] if most_common else my_list[0]

def compare_entities(entity1, entity2):
    prompt = f"""Compare the following two entities, you job is to determine if the entity are the same based on your undersanding of the description and type.
    
    Entity 1:
    Name: {entity1[0]}
    Type: {entity1[1]}
    Description: {entity1[2]}
    
    Entity 2:
    Name: {entity2[0]}
    Type: {entity2[1]}
    Description: {entity2[2]}
    
    Are these entities the same? Answer 'yes' or 'no'."""
    
    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": prompt}],
        max_tokens=2000,
        temperature=0.1,
    )
    answer = response.choices[0].message.content.lower()
    
    if 'yes' in answer:
        return True
    return False

def entities_and_relationships_resolution(input_file, output_file):
    # Read input JSONL file
    data = read_jsonl(input_file)

    # Parse the input data
    entities, relationships = parse_input(data)

    # Remove duplicates based on name 
    unique_entities = remove_duplicates(entities)

    # calculate embeddings for each entity
    for i, entity in enumerate(unique_entities):
        embedding = calculate_embedding('name: ' + entity[0] + 'type: ' + entity[1] + 'description: ' + entity[2])
        unique_entities[i] = (entity[0], entity[1], entity[2], entity[3], embedding)

    # Calculate embeddings for all entity
    embeddings = np.array([entity[4] for entity in unique_entities])

    # Construct similarity graph using cosine similarity
    similarity_matrix = cosine_similarity(embeddings)
    np.fill_diagonal(similarity_matrix, 0)  # Remove self-similarity
    edges = np.argwhere(similarity_matrix > 0)
    weights = similarity_matrix[edges[:, 0], edges[:, 1]]

    # Create igraph graph
    g = ig.Graph()
    g.add_vertices(len(unique_entities))
    g.add_edges(edges)
    g.es['weight'] = weights

    # Apply Leiden Algorithm
    partition = la.find_partition(g, la.CPMVertexPartition, weights='weight', resolution_parameter=2.0)


    # Organize entity by cluster labels
    clusters = {}
    for idx, cluster_id in enumerate(partition.membership):
        if cluster_id not in clusters:
            clusters[cluster_id] = []
        clusters[cluster_id].append(unique_entities[idx])
    
    # Entity Resolution
    entity_mapping = {}
    entity2doc = defaultdict(list)

    for key in clusters:
        group = clusters[key]
        names = [item[0] for item in group]
        common_value = most_common_or_first(names)
        for name in names:
            entity_mapping[name] = common_value

    # Entity Resolution    
    normalized_entities = [
    {
        "name": entity_mapping.get(name, name),
        "type": entity_type,
        "description": description,
        "original_text": original_text,
        "doc_id": doc_id,
        "filename": filename,
    }
    for name, entity_type, description, original_text, doc_id, filename in entities
    ]
    # collect the doc_id for each entity
    for entity in normalized_entities:
        entity2doc[entity['name']].append(entity['doc_id'])

    # Normalize and adjust relationships
    normalized_relationships = []

    for relationship in relationships:
        source, target, description, strength, original_text, doc_id, filename = relationship
        normalized_source = entity_mapping[source] if source in entity_mapping else source
        normalized_target = entity_mapping[target] if target in entity_mapping else target
        normalized_relationships.append({
            "doc_id": doc_id,
            "filename": filename,
            "source": normalized_source,
            "target": normalized_target,
            "description": description,
            "strength": strength,
            "text": original_text
        })

    # Prepare final output data
    entity_output_file = output_file.replace('.jsonl', '_entities.jsonl')
    relationship_output_file = output_file.replace('.jsonl', '_relationships.jsonl')

    # Write to output JSONL file
    write_jsonl(entity_output_file, normalized_entities)
    write_jsonl(relationship_output_file, normalized_relationships)
    print(f'Resolution entities and relationships have been written to {output_file}')

    # save entity_map for debugging
    with open('jsonl/entity_resolution_mapping.json', 'w') as json_file:
        json.dump(entity_mapping, json_file, indent=4)
     # save entity_map for debugging
    with open('jsonl/entity_to_doc.json', 'w') as json_file:
        json.dump(entity2doc, json_file, indent=4)

    print("Dictionary saved to entity_resolution_mapping.json")

if __name__ == "__main__":
    input_file = 'jsonl/raw_entity.jsonl'
    output_file = 'jsonl/resolution.jsonl'

    entities_and_relationships_resolution(input_file, output_file)

    
