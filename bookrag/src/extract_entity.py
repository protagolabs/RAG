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

def extract_entity(document):
    prompt = f"""

    Given a text document that is potentially relevant to this activity and a list of entity types with description, identify all entities of those types from the text and all relationships among the identified entities.
    
    - entity_type and their description:

    Person: Includes individual characters such as Harry Potter, Hermione Granger, and Albus Dumbledore.
    Location: Includes places like Hogwarts, Diagon Alley, and the Forbidden Forest.
    Organization: Includes entities such as Hogwarts School of Witchcraft and Wizardry and Gringotts Bank.
    Event: Includes significant occurrences such as the Sorting Ceremony and the Quidditch matches.
    Magical Creature: Includes entities like centaurs, trolls, and goblins.
    Magical Object: Includes items like the Sorcerer's Stone, wands, and the Mirror of Erised.
    Spell: Includes magical incantations and charms used by characters.
    Title: Titles or roles such as Professor, Head Boy, or Headmaster.
    House: Refers to the different houses at Hogwarts like Gryffindor, Slytherin, etc.
    Other: Any entity that does not fit into the above categories.

    -Steps-
    1. Identify all entities. For each identified entity, extract the following information:
    - entity_name: Name of the entity, capitalized
    - entity_type: entity_type: One of the types mentioned above: [Person, Location, Organization, Event, Magical Creature, Magical Object, Spell, Title, House, Other]
    - entity_description: Comprehensive description of the entity's attributes and activities
    Format each entity as 
    entity{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>

    2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
    For each pair of related entities, extract the following information:
    - source_entity: name of the source entity, as identified in step 1
    - target_entity: name of the target entity, as identified in step 1
    - relationship_description: explanation as to why you think the source entity and the target entity are related to each other
    - relationship_strength: an integer score between 1 to 10, indicating strength of the relationship between the source entity and target entity
    
    Format each relationship as 
    relationship{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>

    3. Return output in Englis as a single list of all the entities and relationships identified in steps 1 and 2. Use **{{record_delimiter}}** as the list delimiter. If you have to translate, just translate the descriptions, nothing else!

    4. When finished, output {{completion_delimiter}}

    
    ######################
    -Examples-
    ######################
    Text:
    Harry successfully defended the Philosopher's Stone {{tuple_delimiter}} He faced Voldemort and prevented him from stealing the Stone. Harry received help from Dumbledore who gave him his father's Cloak and taught him enough to help in the situation.
    ################
    Output:
    
    entity{{tuple_delimiter}}HARRY POTTER{{tuple_delimiter}}Person{{tuple_delimiter}}Harry Potter is a young wizard known for defeating Voldemort as a baby and later facing him multiple times.
    entity{{tuple_delimiter}}PHILOSOPHER'S STONE{{tuple_delimiter}}Magical Object{{tuple_delimiter}}The Philosopher's Stone is a legendary alchemical substance capable of turning any metal into pure gold and producing the Elixir of Life, which grants immortality.
    entity{{tuple_delimiter}}VOLDEMORT{{tuple_delimiter}}Person{{tuple_delimiter}}Voldemort is a dark wizard known for his attempts to conquer the wizarding world and his repeated confrontations with Harry Potter.
    entity{{tuple_delimiter}}DUMBLEDORE{{tuple_delimiter}}Person{{tuple_delimiter}}Albus Dumbledore is the headmaster of Hogwarts School of Witchcraft and Wizardry, known for his wisdom and powerful magic.
    entity{{tuple_delimiter}}CLOAK{{tuple_delimiter}}Magical Object{{tuple_delimiter}}The Cloak is an Invisibility Cloak that once belonged to Harry Potter's father, allowing the wearer to become invisible.

    relationship{{tuple_delimiter}}HARRY POTTER{{tuple_delimiter}}PHILOSOPHER'S STONE{{tuple_delimiter}}Harry defended the Philosopher's Stone from being stolen by Voldemort.{{tuple_delimiter}}5
    relationship{{tuple_delimiter}}HARRY POTTER{{tuple_delimiter}}VOLDEMORT{{tuple_delimiter}}Harry faced Voldemort and prevented him from stealing the Philosopher's Stone.{{tuple_delimiter}}5
    relationship{{tuple_delimiter}}HARRY POTTER{{tuple_delimiter}}DUMBLEDORE{{tuple_delimiter}}Dumbledore helped Harry by giving him his father's Cloak and teaching him enough to help in the situation.{{tuple_delimiter}}4
    relationship{{tuple_delimiter}}HARRY POTTER{{tuple_delimiter}}CLOAK{{tuple_delimiter}}Harry received the Cloak from Dumbledore to aid in his quest.{{tuple_delimiter}}3
    relationship{{tuple_delimiter}}DUMBLEDORE{{tuple_delimiter}}CLOAK{{tuple_delimiter}}Dumbledore gave Harry the Invisibility Cloak that belonged to Harry's father.{{tuple_delimiter}}4

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
        doc_id, filename, document_text = doc.values()
        lines = document_text.split('\n')
        for line in lines:
            if len(line) > 30: # Only consider lines with reasonable length and meaning, 30 is for character length, not token
                line = standardize_delimiter(line)
                answer = extract_entity(line)
                results.append({'doc_id': doc_id, 'filename':filename, 'document': line, 'entity': answer})
    
    # Reduce step: write the results to the output JSONL file
    with jsonlines.open(output_file, mode='w') as writer:
        for result in results:
            writer.write(result)

if __name__ == "__main__":
    # extract entity
    input_file = '../jsonl/raw_summary.jsonl'
    output_file = '../jsonl/raw_entity.jsonl'  
    save_entity(input_file, output_file)