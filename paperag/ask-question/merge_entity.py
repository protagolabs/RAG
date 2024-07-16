import json
import jsonlines
from openai import OpenAI
import torch
import ollama
import re

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
            if parts[0] == "entity":
                entities.append((parts[1], parts[2], parts[3], record['document']))
            elif parts[0] == "relationship":
                relationships.append((parts[1], parts[2], parts[3], int(parts[4]), record['document']))
    
    return entities, relationships

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

def merge_entities_and_relationships(input_file, output_file):
    # Read input JSONL file
    data = read_jsonl(input_file)

    # Parse the input data
    entities, relationships = parse_input(data)

    # Merge entities based on comparison
    merged_entities = []
    skip_indices = set()
    entity_mapping = {}

    for i, entity1 in enumerate(entities):
        if i in skip_indices:
            continue
        # Start with the current entity
        merged_entity = entity1
        
        for j in range(i + 1, len(entities)):
            if j in skip_indices:
                continue
            
            entity2 = entities[j]
            if compare_entities(entity1, entity2):
                # Add index j to skip_indices since entity2 is being merged
                skip_indices.add(j)

                # Record the mapping of the removed entity to the remaining entity
                entity_mapping[entity2] = entity1
                
                # Optional: Update merged_entity based on your merge logic
                # For instance, here we simply retain entity1's data.
                # If you have a specific merge logic, implement it here.

        merged_entities.append(merged_entity)

    # Normalize entities
    normalized_entities = [
        {
            "name": name,
            "type": entity_type,
            "description": description,
            "original_text": original_text
        }
        for name, entity_type, description, original_text in merged_entities
    ]
    # Normalize and adjust relationships
    normalized_relationships = []

    for relationship in relationships:
        source, target, description, strength, original_text = relationship.values()
        normalized_source = entity_mapping[source] if source in entity_mapping else source
        normalized_target = entity_mapping[target] if target in entity_mapping else target
        normalized_relationships.append({
            "type": "relationship",
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
    write_jsonl(normalized_entities, entity_output_file)
    write_jsonl(normalized_relationships, relationship_output_file)
    print(f'Merged entities and relationships have been written to {output_file}')

    # save entity_map for debugging
    with open('jsonl/entity_mapping.json', 'w') as json_file:
        json.dump(entity_mapping, json_file, indent=4)

    print("Dictionary saved to entity_mapping.json")

if __name__ == "__main__":
    input_file = 'jsonl/raw_entity.jsonl'
    output_file = 'jsonl/merge.jsonl'

    merge_entities_and_relationships(input_file, output_file)

    
