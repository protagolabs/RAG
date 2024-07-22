import json
import jsonlines
from openai import OpenAI
import torch
import os
import numpy as np
import re
import copy
from collections import defaultdict
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_feature_engineer_templates(ENTITY_RESOLUTION, document_text):
    """
    Generates FEATURE_ENGINEER template with substituted texts.
    
    """

    # Deep copy the original template to avoid modifying it
    updated_template = copy.deepcopy(ENTITY_RESOLUTION)
        
    # Substitute the placeholder in the user document
    for entry in updated_template:
        if entry["role"] == "user":
            entry["content"] = entry["content"].format(document=document_text)
    
    return updated_template

# Define the tuple delimiter used in the input
tuple_delimiter = "{tuple_delimiter}"

def standardize_delimiter(input_string, standard_delimiter="{tuple_delimiter}"):
    # Define the regex pattern to match any case variation of {tuple_delimiter}
    pattern = re.compile(r'\{tuple_delimiter\}', re.IGNORECASE)
    
    # Replace all variations with the standard delimiter
    standardized_string = pattern.sub(standard_delimiter, input_string)
    
    return standardized_string


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
        name, typ = item[0],item[1]
        if name not in unique_items:
            unique_items[name] = (item[0],item[1],item[2])
        # if (name,typ) not in unique_items:
        #     unique_items[(name,typ)] = (item[0],item[1].lower(),item[2])
    return list(unique_items.values())


def run_openai(messages):
    
    # Send the prompt to OpenAI's GPT-4
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000,
        stop=None,
        temperature=0.7
    )

    answer = response.choices[0].message.content
    
    return answer
    

def entities_and_relationships_resolution(input_file, output_file):
    # Read input JSONL file
    data = read_jsonl(input_file)

    # Parse the input data
    entities, relationships = parse_input(data)

    # Remove duplicates based on name 
    unique_entities = remove_duplicates(entities)

    # Group entities by type
    # Initialize a dictionary to group by type
    grouped_data = defaultdict(list)

    # Iterate through the original list and group by type
    for item in unique_entities:
        _, item_type, description = item
        grouped_data[item_type].append(item)

    # Entity Resolution
    entity_mapping = {}
    entity2doc = defaultdict(list)
    entity2description = defaultdict(list)

    for key in grouped_data:
        document = str(grouped_data[key])
        updated_template = generate_feature_engineer_templates(ENTITY_RESOLUTION, document)
        answer = run_openai(updated_template)
        answer = answer.split('\n')
        for ans in answer:
            if '{{same}}' in ans:
                ans = ans.split('{{same}}')
                for i in range(1,len(ans)):
                    entity_mapping[ans[i].strip()] = ans[0].strip()

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
        entity2description[entity['name']].append(entity['description'])

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
    with open('jsonl/entity_group_type.json', 'w') as json_file:        
        json.dump(grouped_data, json_file, indent=4)
    with open('jsonl/entity_resolution_mapping.json', 'w') as json_file:
        json.dump(entity_mapping, json_file, indent=4)
    with open('jsonl/entity_to_doc.json', 'w') as json_file:
        json.dump(entity2doc, json_file, indent=4)
    with open('jsonl/entity_to_description.json', 'w') as json_file:        
        json.dump(entity2description, json_file, indent=4)

    print("Dictionary saved to entity_resolution_mapping.json")

ENTITY_RESOLUTION = [
    {"role" : "system",
     "content": """
        ---Role---
        You are an assistant with expertise in natural language processing and entity resolution.

        ---Goal---
        Your task is to identify and point out entities within the provided document that refer to the same entity, even if their names are slightly different. The goal is to group these entities together for clarity and consistency.

        ---Guidelines---
        - Carefully read through the document and identify entities of the specified type that refer to the same thing.
        - Compare descriptions to ensure accurate grouping.
        - Provide the output in the format: 
        name_x {{same}} name_o {{same}} name_g
        name_ww {{same}} name_x
        - Ensure accuracy and completeness in grouping the entities.
        - Each time, you will be given a single type of entity to determine.
        - When finished, output {{completion_delimiter}}

        ---Example---
        Input: 
        [('MR. DURSELY', 'person', 'Mr. Dursley is a director of a drilling firm and takes pride in his normality.'),
        ('MR. DURSLEY', 'person', "Mr. Dursley is Harry Potter's uncle and a non-magical person who disbelieves in anything supernatural."),
        ('HARRY', 'person', 'Harry is a young wizard known for defeating Voldemort as a baby and later facing him multiple times.'),
        ('HARRY POTTER', 'person', "Harry Potter is a young wizard known for surviving Lord Voldemort's attack as a baby. He is famous throughout the wizarding world for his bravery and magical abilities."),
        ('HARRY potter', 'person', "Harry potter is a young wizard who is surviving Lord Voldemort's attack, lived with his aunt.")]
        
        Output: 
        MR. DURSELY {{same}} MR. DURSLEY
        HARRY {{same}} HARRY POTTER {{same}} HARRY potter

         {{completion_delimiter}}

        

    """},
    {"role": "user",
    "content": """
        ---Input---
        Here is the document: 

        {document}
"""}]

if __name__ == "__main__":
    input_file = 'jsonl/raw_entity.jsonl'
    output_file = 'jsonl/resolution.jsonl'

    entities_and_relationships_resolution(input_file, output_file)

    
