from dotenv import load_dotenv
from openai import OpenAI
import copy
import json
import uuid
import os
import re

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def format_conversation(conversation):
    """Formats the conversation list into a cohesive text block."""
    return " ".join(conversation)

def generate_feature_engineer_templates(FEATURE_ENGINEER, conversation_text):
    """
    Generates FEATURE_ENGINEER template with substituted texts.
    
    """

    # Deep copy the original template to avoid modifying it
    updated_template = copy.deepcopy(FEATURE_ENGINEER)
        
    # Substitute the placeholder in the user content
    for entry in updated_template:
        if entry["role"] == "user":
            entry["content"] = entry["content"].format(text=conversation_text)
    
    return updated_template

def extract_dict_from_json(text: str):
        """
        Extract the dictionary between "```json" and "```". 
        """
        pattern = r'```json(.*?)```'
        extracted_text = re.findall(pattern, text, re.DOTALL)
        extracted_text = extracted_text[0].strip()
        extracted_text = json.loads(extracted_text)

        return extracted_text

# Function to get embedding for a given text
def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

def analyze_conversation_gpt4(messages):
    # Generate a unique conversation ID
    conversation_id = str(uuid.uuid4())
    conversation_details = {
        "conversation_id": conversation_id,
    }
    
    # Send the prompt to OpenAI's GPT-4
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7
    )

    # extract dictionary from string output
    conversation_analysis = response.choices[0].message.content
    conversation_analysis = extract_dict_from_json(conversation_analysis)
    
    # Merge the two dictionaries
    combined_json = {**conversation_details, **conversation_analysis}

    # Print the full text output from GPT-4
    return combined_json



def process_jsonl_file(file_path, output_file):
    """Process each conversation in a .jsonl file and save the results to a JSONL file."""
    with open(file_path, 'r') as file, open(output_file, 'w') as outfile:
        for line in file:
            data = json.loads(line)
            conversation = format_conversation(data['conversation'])
            updated_template = generate_feature_engineer_templates(FEATURE_ENGINEER, conversation)
            result = analyze_conversation_gpt4(updated_template)
            json.dump(result, outfile)  # Write the JSON object to the file
            outfile.write('\n')  # Write a newline to separate JSON objects

FEATURE_ENGINEER = [
    {"role" : "system",
     "content": """Now, you are an analysis assistant who can help users extract and structure information from conversation transcripts.
    ## You must follow all the requirements to modify the draft:
        1. Summarize the conversation, identifying the key roles and actions.
        2. Analyze the sentiment expressed by each participant throughout the conversation using words or short phrases.
        3. Identify the intent behind the conversation using a clear, concise phrase.
        4. Describe the emotions displayed by each participant at different stages of the conversation using words or lists of words.
        5. Determine the main topics discussed using short phrases.

    ## About the output:
        Your output must be a JSON file containing a Python dictionary to store the extracted information in the format as shown below:
        
        {{
            "summary": "text_summary_of_the_conversation",
            "sentiment": {{
                "Participant1": "descriptive_sentiment",
                "Participant2": {
                    "initial": "initial_sentiment",
                    "shift": "shifted_sentiment"
                }
            }},
            "intent": "primary_intent_of_the_conversation",
            "emotion": {{
                "Participant1": ["emotion1", "emotion2", "..."],
                "Participant2": ["emotion1", "emotion2", "..."]
            }},
            "topic": "main_topic_discussed"
        }}
        You must follow all requirements listed above. 
        Your output must contain the json file quoted by "```json" and "```"
    """},
    {"role": "user",
    "content": """
        The given text is:

    {text}
"""}]

# Example of using the mathSolve
if __name__ == "__main__":
    # Example usage
    # conversation_text = """
    # Person A: Hey man , you wanna buy some weed ?", "Person B: Some what ?", "Person A: Weed ! You know ? Pot , Ganja , Mary Jane some chronic !", "Person B: Oh , umm , no thanks .", "Person A: I also have blow if you prefer to do a few lines .", "Person B: No , I am ok , really .", "Person A: Come on man ! I even got dope and acid ! Try some !", "Person B: Do you really have all of these drugs ? Where do you get them from ?", "Person A: I got my connections ! Just tell me what you want and I ' ll even give you one ounce for free .", "Person B: Sounds good ! Let ' s see , I want .", "Person A: Yeah ?", "Person B: I want you to put your hands behind your head ! You are under arrest !
    # """
    # updated_template = generate_feature_engineer_templates(FEATURE_ENGINEER, conversation_text)
    # result = analyze_conversation_gpt4(updated_template)
    # print(result)

    # Path to your .jsonl file and output file
    jsonl_file_path = '../sample_data/conversations_test.jsonl'
    output_json_path = 'results.json'
    process_jsonl_file(jsonl_file_path, output_json_path)