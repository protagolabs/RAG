import json
import jsonlines
from openai import OpenAI
import torch
import ollama
import re
from datasets import load_dataset

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

def extract_entity(document):
    prompt = f"""

    Given a text document that is potentially relevant to this activity and a list of entity types with description, identify all entities of those types from the text.
    
    - entity_type and their description:

    Definitions and Concepts: Explanations or interpretations of terms, concepts, and abstract ideas.
    Events and History: Significant occurrences, happenings, and historical events.
    Health and Medicine: Aspects related to physical or mental well-being, including diseases, treatments, and wellness.
    Business and Finance: Information related to companies, commerce, finance, economics, and employment.
    Products and Services: Items or services available for sale, including consumer goods and software.
    Science and Technology: The systematic study of the natural world and the application of scientific knowledge for practical purposes, especially in industry.
    People and Roles: Information about individuals, including personal details, occupations, and roles.
    Geography and Locations: Information related to geographical areas, places, countries, and their features.
    Education and Academia: Aspects related to learning, teaching, academic institutions, and research.
    Media and Creative Works: Creative expressions, including art, literature, music, films, and other media.
    Actions and Processes: Specific activities, behaviors, processes, methods, or procedures.
    Community and Society: Social groups, networks, cultural aspects, and societal norms.
    Law and Legal Concepts: Aspects related to laws, regulations, governance, and legal proceedings.
    Weather and Environment: Meteorological conditions, environmental aspects, and natural phenomena.
    Food and Nutrition: Aspects related to culinary arts, food preparation, and nutritional information.
    Spirituality and Religion: Concepts and beliefs related to spirituality, religion, and philosophical ideas.
    Art and Entertainment: Visual arts, entertainment, sports, and other leisure activities.

    -Steps-
    1. Identify all entities. For each identified entity, extract the following information:
    - entity_name: Name of the entity, capitalized
    - entity_type: entity_type: One of the types mentioned above: [Person, Location, Organization, Event, Magical Creature, Magical Object, Spell, Title, House, Other]
    - entity_description: Comprehensive description of the entity's attributes and activities
    Format each entity as 
    <entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>

    2. Return output in Englis as a single list of all the entities in steps 1.

    3. When finished, output {{completion_delimiter}}, DO NOT OUTPUT OTHER TEXTS.

    
    ######################
    -Examples-
    ######################
    Text:
    Global Business Dubai Opens a Tower to Beat All By LANDON THOMAS Jr. JAN. 4, 2010A visitor gets a view of Dubai from the 124th floor of Burj Khalifa, the world’s tallest building, on Monday. Ali Haider/European Pressphoto Agency Burdened by debt and a devastating real estate crash, Dubai is doing what it does best: doubling down. Just one month after a close brush with bankruptcy, Dubai celebrated the opening of the world’s tallest building on Monday — a rocket-shaped edifice that soars 2,717 feet and has views that reach 60 miles. The glittering celebration may have been an attempt by Dubai’s ruler, Sheik Mohammed bin Rashid al-Maktoum, to shift the focus from Dubai’s current economic troubles to a future filled with more promise. All the same, the tower’s success by no means signals a recovery in Dubai’s beaten-down real estate market, where prices have collapsed by as much as 50 percent and many developers are having trouble finding occupants for their buildings. With its mix of nightclubs, mosques, luxury suites and boardrooms, the Burj is an almost perfect representation of Dubai’s own complexities and contradictions. It will have the world’s first Armani hotel; the world’s highest swimming pool, on the 76th floor; the highest observation deck, on the 124th floor; and the highest mosque, on the 158th floor. Related Coverage The World’s Tallest Building JAN. 4, 2010Fireworks Greet Tallest Skyscraper But in deciding to change the tower’s name from Burj Dubai to Burj Khalifa, in honor of the president of the United Arab Emirates, Sheik Khalifa bin Zayed al-Nahyan, Dubai revealed a rare streak of humility consistent with its diminished economic condition. Once the most proudly autonomous of Arab Emirates, Dubai has found that its financial troubles have made it more dependent on Abu Dhabi and more likely to be drawn closer into the federation.
    ################
    Output:
    
    Global Business Dubai{{tuple_delimiter}}Business and Finance{{tuple_delimiter}}An overview of the business activities and financial aspects related to Dubai, including its economic challenges and recovery efforts.
    Landon Thomas Jr.{{tuple_delimiter}}People and Roles{{tuple_delimiter}}The author of the article discussing Dubai's economic and architectural developments.
    JAN. 4, 2010{{tuple_delimiter}}Events and History{{tuple_delimiter}}The date when the Burj Khalifa was officially opened and the article was published.
    Dubai{{tuple_delimiter}}Geography and Locations{{tuple_delimiter}}A city in the United Arab Emirates known for its skyscrapers, luxury shopping, and vibrant nightlife.
    Burj Khalifa{{tuple_delimiter}}Products and Services{{tuple_delimiter}}The world's tallest building, standing at 2,717 feet with features like an observation deck, luxury suites, and the highest swimming pool and mosque.
    Ali Haider/European Pressphoto Agency{{tuple_delimiter}}People and Roles{{tuple_delimiter}}The photographer or agency credited with the accompanying photo in the article.
    Sheik Mohammed bin Rashid al-Maktoum{{tuple_delimiter}}People and Roles{{tuple_delimiter}}The ruler of Dubai, involved in the city's economic and infrastructural development.
    Economic troubles{{tuple_delimiter}}Business and Finance{{tuple_delimiter}}Refers to the financial difficulties faced by Dubai, including a real estate crash and a brush with bankruptcy.
    Bankruptcy{{tuple_delimiter}}Business and Finance{{tuple_delimiter}}A financial state that Dubai narrowly avoided, indicating severe economic distress.
    Real estate market{{tuple_delimiter}}Business and Finance{{tuple_delimiter}}The sector in Dubai that experienced a significant collapse, with property prices dropping by up to 50%.
    Armani hotel{{tuple_delimiter}}Products and Services{{tuple_delimiter}}A luxury hotel located within the Burj Khalifa, known for its high-end design and services.
    Sheik Khalifa bin Zayed al-Nahyan{{tuple_delimiter}}People and Roles{{tuple_delimiter}}The president of the United Arab Emirates, after whom the Burj Khalifa was named, showing a gesture of respect and acknowledgment.
    Abu Dhabi{{tuple_delimiter}}Geography and Locations{{tuple_delimiter}}The capital of the United Arab Emirates, noted for its financial support and influence over Dubai during economic hardships.
    The World’s Tallest Building{{tuple_delimiter}}Media and Creative Works{{tuple_delimiter}}An article or piece discussing the Burj Khalifa and its significance.
    Fireworks Greet Tallest Skyscraper{{tuple_delimiter}}Media and Creative Works{{tuple_delimiter}}An event celebrating the inauguration of the Burj Khalifa with fireworks.

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
    
    # CONTINUE_PROMPT = """
    # SOME entities might missed in the last extraction. find them based on previous entity types list.
    # Output all entities using the same format:
    
    # <entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>
    # <entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>
    # <entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>

    # {{completion_delimiter}}
    
    # DO NOT OUTPUT OTHER TEXTS.
    # """
    # new_prompt = prompt + '\n' + answer + '\n' + CONTINUE_PROMPT
    # response = client.chat.completions.create(
    #     model='gemma2',
    #     messages=[{"role": "system", "content": new_prompt}],
    #     temperature=0.1,
    # )
    # new_answer = response.choices[0].message.content

    return answer

def save_entity(output_file):
    # load dataset
    passages = load_dataset("UKPLab/dapr", "MSMARCO-corpus", split="test")
    with jsonlines.open(output_file, mode='w') as writer:
        for passage in passages:
            text = passage['text']
            _id = passage['_id']
            doc_id = passage['doc_id']
            answer = extract_entity(text)
            result = {'_id': _id, 'doc_id':doc_id, 'entity': answer}
            writer.write(result)

if __name__ == "__main__":
    # extract entity
    output_file = '../jsonl/raw_entity.jsonl'  
    save_entity(input_file, output_file)