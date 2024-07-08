import os
from openai import OpenAI
from rds import MySQLConnection
from milvus import connect_to_milvus
from dotenv import load_dotenv
import json
# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to get embedding for a given text
def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

def setup_database():
    # Initialize the MySQL connection
    db = MySQLConnection()
    db.connect_to_database('rag')

    # Create necessary tables
    conversations_schema = """
        conversation_id VARCHAR(36) PRIMARY KEY,
        conversation JSON,
        summary TEXT,
        intent TEXT
    """
    tags_schema = """
        tag_id INT AUTO_INCREMENT PRIMARY KEY,
        conversation_id VARCHAR(36) UNIQUE,
        sentiment TEXT,
        emotion TEXT,
        topic VARCHAR(255),
        FOREIGN KEY (conversation_id) REFERENCES Conversations(conversation_id)
    """

    # delete existing table
    #db.delete_table('Tags')
    #db.delete_table('Conversations')
    

    # Connect to database, create tables
    #db.create_table('Conversations', conversations_schema)
    #db.create_table('Tags', tags_schema)
    return db

# Sample conversation data
conversation_data = {
    "conversation_id": "f98aa0a2-d461-431b-a8a2-efefba16f142",
    "conversation": [
        "Person A: Why'd you pull me over?",
        "Person B: Are you aware that you drove through a red light?",
        "Person A: I ran a red light?",
        "Person B: Yes, you did.",
        "Person A: I apologize, but I didn't realize that I did.",
        "Person B: Weren't you taught that yellow means slow down, not speed up?",
        "Person A: I did learn that.",
        "Person B: So, then why did you speed up?",
        "Person A: I don't know what to tell you.",
        "Person B: I'm going to have to write you a ticket.",
        "Person A: I understand.",
        "Person B: Here you go. Don't do that again."
    ],
    "summary": "Traffic stop for running a red light",
    "sentiment": ["apologetic","authoritative"],
    "intent": "Issue a traffic ticket",
    "emotion": ["confused", "apologetic"],
    "topic": "Traffic violation"
}


conversation_data = {
    "conversation_id": "f98aa0a2-d461-431b-a8a2-efefba16f142",
    "conversation": json.dumps([
        "Person A: Why'd you pull me over?",
        "Person B: Are you aware that you drove through a red light?",
        "Person A: I ran a red light?",
        "Person B: Yes, you did.",
        "Person A: I apologize, but I didn't realize that I did.",
        "Person B: Weren't you taught that yellow means slow down, not speed up?",
        "Person A: I did learn that.",
        "Person B: So, then why did you speed up?",
        "Person A: I don't know what to tell you.",
        "Person B: I'm going to have to write you a ticket.",
        "Person A: I understand.",
        "Person B: Here you go. Don't do that again."
    ]),
    "summary": "Traffic stop for running a red light",
    "intent": "Issue a traffic ticket",
}

# Data for Tags table
tag_data = {
    "conversation_id": "f98aa0a2-d461-431b-a8a2-efefba16f142",
    "sentiment": "apologetic,authoritative",
    "emotion": "confused,apologetic",
    "topic": "Traffic violation"
}


# Example usage
if __name__ == "__main__":
    # Initialize database connection and setup tables
    db = setup_database()
    #print(db.list_tables())
    

    # delete pre-existing data
    # conditions = {"conversation_id": "f98aa0a2-d461-431b-a8a2-efefba16f142"}
    # db.delete_data("Tags", conditions)
    # db.delete_data("Conversations", conditions)
    #db.read_data("Tags", conditions)

    # Insert data into Conversations and Tags
    db.insert_data('Conversations', conversation_data, primary_key='conversation_id')
    db.insert_data('Tags', tag_data, primary_key='conversation_id')

    results = db.search_data('Tags', 'confused', ['topic', 'emotion', 'sentiment'])
    print(results)