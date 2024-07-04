import json
from datasets import load_dataset

# Read the text file
with open('dialogues_test.txt', 'r') as file:
    lines = file.readlines()

# Function to convert a conversation line into a JSON object with speaker info
def convert_to_json_with_speakers(conversation_line):
    # Remove trailing '\n' and any trailing ' __eou__'
    conversation_line = conversation_line.rstrip().rstrip(' __eou__')
    
    # Split the line by '__eou__' to get individual utterances
    utterances = conversation_line.split(' __eou__ ')
    # Remove any empty strings from the list of utterances
    utterances = [utt.strip() for utt in utterances if utt.strip()]
    
    # Add speaker information (assuming alternating speakers)
    conversation = []
    speakers = ["Person A", "Person B"]
    for i, utt in enumerate(utterances):
        # Replace unicode escape sequence \u2019 with the appropriate character
        utt = utt.replace('\u2019', "'")
        speaker = speakers[i % 2]
        conversation.append(f"{speaker}: {utt}")
    
    # Create a JSON object with the conversation
    return {"conversation": conversation}

# List to hold all the JSON objects
json_list = []

# Convert each line into a JSON object and add to the list
for line in lines:
    json_obj = convert_to_json_with_speakers(line)
    json_list.append(json_obj)

path_to_jsonl = 'conversations_test.jsonl'
# Write the JSON objects to a JSONL file
with open(path_to_jsonl, 'w') as jsonl_file:
    for json_obj in json_list:
        jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + '\n')

print("Conversion to JSONL with speakers completed.")


# Load your dataset
dataset = load_dataset('json', data_files=path_to_jsonl)

dataset.push_to_hub("elricwan/dailydialog_test", private=False)
