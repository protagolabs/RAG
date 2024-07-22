import json
import jsonlines
from openai import OpenAI
from collections import defaultdict
import copy
import torch
import ollama
import networkx as nx
from .entity_resolution import standardize_delimiter
from .milvus_database import connect_to_milvus, create_index, search_entity_by_embedding_and_type, search_relationship_by_embedding

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

tuple_delimiter = '{tuple_delimiter}'

# Function to calculate embedding for each point
def calculate_embedding(point):
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=point)["embedding"]
    return embedding

def query_to_entity(Query):
    prompt = f"""

    Given a user query text that is potentially relevant to this activity and a list of entity types with descriptions, identify all entities of those types from the text and any actions/events described.

    - Entity types and their descriptions:

    Person: Includes individual characters such as Harry Potter, Hermione Granger, and Albus Dumbledore.
    Location: Includes places like Hogwarts, Diagon Alley, and the Forbidden Forest.
    Organization: Includes entities such as Hogwarts School of Witchcraft and Wizardry and Gringotts Bank.
    Event: Includes significant occurrences such as the Sorting Ceremony and the Quidditch matches.
    Magical Creature: Includes entities like centaurs, trolls, and goblins.
    Magical Object: Includes items like the Sorcerer's Stone, wands, and the Mirror of Erised.
    Spell: Includes magical incantations and charms used by characters.
    Title: Titles or roles such as Professor, Head Boy, or Headmaster.
    House: Refers to the different houses at Hogwarts like Gryffindor, Slytherin, etc.
    Action/Event: Any verb or occurrence that describes what entities do or what happens to them, such as "fight," "friendship," "explore," etc.
    
    - Steps -
    1. Identify all entities and actions/events. For each identified entity or action/event, extract the following information:
    - entity_name: Name of the entity or action/event, capitalized
    - entity_type: One of the types mentioned above: [Person, Location, Organization, Event, Magical Creature, Magical Object, Spell, Title, House, Action/Event, Other]
    
    Format each entity or action/event as:
    <entity_name>{{tuple_delimiter}}<entity_type>

    2. When finished, output {{completion_delimiter}}

    ######################
    - Examples -
    ######################
    Text:
    'Who are the friends of Harry Potter?'
    ################
    Output:
    
    HARRY POTTER{{tuple_delimiter}}Person
    FRIENDS{{tuple_delimiter}}Action/Event
    
    {{completion_delimiter}}

    - Text Document -
    ######################
    {Query}

    """



    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": prompt}],
        max_tokens=500,
        n=1,
        temperature=0.1,
    )
    answer = response.choices[0].message.content

    CONTINUE_PROMPT = """
    SOME entities were missed in the last extraction. entity_type must follow the format below:
    - entity_type and their description:

    Person
    Location
    Organization
    Event
    Magical Creature
    Magical Object
    Spell
    Title
    House
    Action/Event
   
   - output format:
    
    <entity_name>{{tuple_delimiter}}<entity_type>

    {{completion_delimiter}}
    
    """
    new_prompt = prompt + '\n' + answer + '\n' + CONTINUE_PROMPT
    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": new_prompt}],
        max_tokens=500,
        n=1,
        temperature=0.1,
    )
    new_answer = response.choices[0].message.content

    return new_answer



def process_query_to_entity(Query, output_file):
    # Connect to Milvus
    connect_to_milvus()
    entity_collection_name = "graphrag_entity_collection"
    relationship_collection_name = "graphrag_relationship_collection"
    # Create indices for collections
    create_index(entity_collection_name, "embedding_of_entity")
    create_index(relationship_collection_name, "embedding_of_relation")

    # Read entity_map to find variant of same entities
    entity_map_file = 'jsonl/entity_resolution_mapping.json'
    with open(entity_map_file, 'r') as file:
        entity_map = json.load(file)
    
    answer = query_to_entity(Query)
    answer = answer.split('\n')
    print(answer)
    with jsonlines.open(output_file, 'w') as writer:
        for line in answer:
            line = standardize_delimiter(line)
            if tuple_delimiter not in line:
                continue
            entity_name, entity_type = line.split(tuple_delimiter)
            if "Action" in entity_type:
                relation_embedding = calculate_embedding(entity_name)
                relationship_results = search_relationship_by_embedding(relationship_collection_name, relation_embedding)
                #print("Relationship search results:")
                for hits in relationship_results:
                    for result in hits:
                        #print(result.get('relationship_description'))
                        writer.write({'relationship_description': result.get('relationship_description')})
            else:
                entity_name_embedding = calculate_embedding(entity_name)
                entity_results = search_entity_by_embedding_and_type(entity_collection_name, entity_name_embedding, entity_type)
                #print("Entity search results:")
                for hits in entity_results:
                    for result in hits:
                        original_name = result.get('entity_name')
                        record_name = entity_map[original_name]
                        #print(result.get('entity_name'))
                        #print(result.get('entity_description'))
                        writer.write({'entity_name': record_name, 'entity_type': entity_type,'entity_description': result.get('entity_description')})

            
            


