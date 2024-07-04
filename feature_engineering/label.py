from dotenv import load_dotenv
from openai import OpenAI
import json
import uuid
import os

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def format_conversation(conversation):
    """Formats the conversation list into a cohesive text block."""
    return " ".join(conversation)

def gpt4_analysis(conversation, task_type):
    """Function to perform different analysis on conversational data using GPT-4.
    
    Args:
    conversation (list): The conversation data.
    task_type (str): Type of analysis ('sentiment', 'ner', 'intent', 'emotion').
    
    Returns:
    str: The model's response.
    """
    formatted_text = format_conversation(conversation)
    prompt_map = {
        "sentiment": f"Analyze the sentiment of the following conversation: {formatted_text}",
        "ner": f"Identify and label the named entities in the following conversation: {formatted_text}",
        "intent": f"Determine the intent of this conversation: {formatted_text}",
        "emotion": f"Determine the emotions expressed in the following conversation: {formatted_text}",
        "question": f"List all questions asked in the following conversation: {formatted_text}",
        "topic": f"Classify the topic of the following conversation: {formatted_text}"
    }

    response = client.chat.completions.create(
        model="gpt-4o",  
        messages=[{"role": "system", "content": prompt_map[task_type]}],
        max_tokens=200
    )
    
    return response.choices[0].message.content


def process_conversation(conversation):
    """Process a single conversation for various NLP tasks and format the output."""
    analysis_result = {
        "conversation_id": str(uuid.uuid4()),  # Generating a unique conversation ID
        "sentiment": gpt4_analysis(conversation, 'sentiment'),
        "intent": gpt4_analysis(conversation, 'intent'),
        "emotion": gpt4_analysis(conversation, 'emotion'),
        "entities": gpt4_analysis(conversation, 'ner'),  # Assuming NER returns JSON
        "questions": gpt4_analysis(conversation, 'question'),
        "topic": gpt4_analysis(conversation, 'topic')
    }
    return analysis_result

def process_jsonl_file(file_path, output_file):
    """Process each conversation in a .jsonl file and save the results to a JSON file."""
    results = []
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            conversation = data['conversation']
            result = process_conversation(conversation)
            results.append(result)
    
    with open(output_file, 'w') as outfile:
        json.dump(results, outfile, indent=4)

# Path to your .jsonl file and output file
jsonl_file_path = '../sample_data/conversations_test.jsonl'
output_json_path = 'results.json'
process_jsonl_file(jsonl_file_path, output_json_path)