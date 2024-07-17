import json
import jsonlines
from openai import OpenAI
import torch
import ollama
import re

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

def extract_entity(document):
    prompt = f"""

    Given a text document that is potentially relevant to this activity, first identify all entities needed from the text in order to capture the information and ideas in the text.
    Next, report all relationships among the identified entities.

    -Steps-
    1. Identify all entities. For each identified entity, extract the following information:
    - entity_name: Name of the entity, capitalized
    - entity_type: Suggest several labels or categories for the entity. The categories should not be specific, but should be as general as possible.
    - entity_description: Comprehensive description of the entity's attributes and activities
    Format each entity as ("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>

    2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
    For each pair of related entities, extract the following information:
    - source_entity: name of the source entity, as identified in step 1
    - target_entity: name of the target entity, as identified in step 1
    - relationship_description: explanation as to why you think the source entity and the target entity are related to each other
    - relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
    Format each relationship as ("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

    3. Return output in Englis as a single list of all the entities and relationships identified in steps 1 and 2. Use **{{record_delimiter}}** as the list delimiter. If you have to translate, just translate the descriptions, nothing else!

    4. When finished, output {{completion_delimiter}}

    5. IMPORTANT: DO NOT USE acronyms or abbreviations. Write out the full name of the entity. Even the original text uses an acronym, write out the full name of the entity if you know it.

    ######################
    -Examples-
    ######################
    Text:
    According to Baidu CEO Robin Li, fully driverless robotaxi rides are predicted to reach 100% in the coming quarters. This suggests that autonomous vehicle technology is rapidly advancing and nearing widespread adoption for commercial use. 
    ################
    Output:
    
    entity{{tuple_delimiter}}ROBIN LI{{tuple_delimiter}}PERSON, EXECUTIVE{{tuple_delimiter}}ROBIN LI is the CEO of Baidu, a leading Chinese technology company. He is known for his leadership and vision in the field of technology, particularly in artificial intelligence and autonomous vehicles.
    entity{{tuple_delimiter}}BAIDU{{tuple_delimiter}}COMPANY, TECHNOLOGY{{tuple_delimiter}}BAIDU is a leading Chinese technology company specializing in Internet-related services and products, artificial intelligence, and autonomous vehicle technology.
    entity{{tuple_delimiter}}ROBOTAXI{{tuple_delimiter}}TECHNOLOGY, TRANSPORTATION{{tuple_delimiter}}ROBOTAXI refers to a fully autonomous vehicle that provides taxi services without a human driver. It is part of the autonomous vehicle technology advancements aimed at revolutionizing transportation.
    entity{{tuple_delimiter}}AUTONOMOUS VEHICLE TECHNOLOGY{{tuple_delimiter}}TECHNOLOGY{{tuple_delimiter}}AUTONOMOUS VEHICLE TECHNOLOGY involves the development and use of self-driving vehicles that can operate without human intervention, using advanced sensors, machine learning, and AI algorithms.
    entity{{tuple_delimiter}}COMMERCIAL USE{{tuple_delimiter}}BUSINESS, APPLICATION{{tuple_delimiter}}COMMERCIAL USE refers to the deployment and utilization of technology for business purposes, including generating revenue and providing services to customers.

    relationship{{tuple_delimiter}}ROBIN LI{{tuple_delimiter}}BAIDU{{tuple_delimiter}}ROBIN LI is the CEO of Baidu and leads the company in its technological advancements, including autonomous vehicle technology.{{tuple_delimiter}}5
    relationship{{tuple_delimiter}}ROBOTAXI{{tuple_delimiter}}AUTONOMOUS VEHICLE TECHNOLOGY{{tuple_delimiter}}ROBOTAXI is a direct application of autonomous vehicle technology, demonstrating its practical use in providing driverless taxi services.{{tuple_delimiter}}4
    relationship{{tuple_delimiter}}AUTONOMOUS VEHICLE TECHNOLOGY{{tuple_delimiter}}COMMERCIAL USE{{tuple_delimiter}}AUTONOMOUS VEHICLE TECHNOLOGY is nearing widespread adoption for commercial use, indicating its readiness for market deployment and customer use.{{tuple_delimiter}}4

    {{completion_delimiter}}

    -Text Document-
    ######################
    {document}

    """

    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": prompt}],
        max_tokens=2000,
        temperature=0.1,
    )
    answer = response.choices[0].message.content
    
    return answer

def save_entity(input_file, output_file):
    # Read the input JSONL file
    with jsonlines.open(input_file, mode='r') as reader:
        documents = [doc for doc in reader]
    
    # Map step: ask the question to each document
    results = []
    for doc in documents:
        document_text = doc['description']  
        answer = extract_entity(document_text)
        results.append({'document': document_text, 'entity': answer})
    
    # Reduce step: write the results to the output JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        for result in results:
            writer.write(result)

if __name__ == "__main__":
    # extract entity
    input_file = 'filtered_ranked_global_data.jsonl'
    output_file = 'jsonl/raw_entity.jsonl'  
    save_entity(input_file, output_file)