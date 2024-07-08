import os
import pymysql
from dotenv import load_dotenv
from typing import List, Dict, Any
import json

# Load environment variables
load_dotenv()

class MySQLConnection:
    def __init__(self):
        self.config = {
            'host': os.getenv('RDS_HOST'),
            'port': int(os.getenv('RDS_PORT')),
            'user': os.getenv('RDS_USER'),
            'password': os.getenv('RDS_PASSWORD'),
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
        }
        self.database = os.getenv('RDS_DATABASE')

    def connect_to_database(self, database_name: str = None):
        config = self.config.copy()
        if database_name:
            config['database'] = database_name
        elif self.database:
            config['database'] = self.database
        return pymysql.connect(**config)

    def create_table(self, table_name: str, schema: str):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()
                print(f"Table {table_name} created or already exists.")

    def insert_data(self, table_name: str, data: Dict[str, Any], primary_key: str = 'id'):
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                if primary_key in data:
                    cursor.execute(f"SELECT 1 FROM {table_name} WHERE {primary_key} = %s", (data[primary_key],))
                    if cursor.fetchone():
                        print(f"Record with {primary_key} = {data[primary_key]} already exists in {table_name}. No insertion performed.")
                        return

                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                cursor.execute(query, list(data.values()))
                conn.commit()
                print(f"Record inserted successfully into {table_name}.")
    def search_data(self, table_name: str, search_term: str, columns: List[str]) -> List[Dict[str, Any]]:
        like_clause = ' OR '.join([f"{col} LIKE %s" for col in columns])
        search_value = f"%{search_term}%"
        query = f"SELECT * FROM {table_name} WHERE {like_clause}"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [search_value] * len(columns))
                results = cursor.fetchall()
                return results if results else []

    def custom_query(self, query, params=None):
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or [])
                results = cursor.fetchall()
                return results
    def read_data(self, table_name: str, conditions: Dict[str, Any]) -> List[Dict[str, Any]]:
        where_clause = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        query = f"SELECT * FROM {table_name} WHERE {where_clause}"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, list(conditions.values()))
                result = cursor.fetchall()
                return result if result else []

    def update_data(self, table_name: str, data: Dict[str, Any], conditions: Dict[str, Any]):
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        where_clause = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        values = list(data.values()) + list(conditions.values())
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, values)
                conn.commit()

    def delete_data(self, table_name: str, conditions: Dict[str, Any]):
        where_clause = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        query = f"DELETE FROM {table_name} WHERE {where_clause}"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, list(conditions.values()))
                conn.commit()
    def search_sentiment(self, table_name: str, person: str, sentiment_value: str):
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                query = f"""
                    SELECT * FROM {table_name}
                    WHERE JSON_UNQUOTE(JSON_EXTRACT(sentiment, '$."{person}"')) = %s
                """
                cursor.execute(query, (sentiment_value,))
                results = cursor.fetchall()
                return results
    def search_person_in_sentiment(self, table_name: str, person: str):
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                query = f"""
                    SELECT * FROM {table_name}
                    WHERE JSON_CONTAINS_PATH(sentiment, 'one', '$."{person}"')
                """
                cursor.execute(query)
                results = cursor.fetchall()
                return results

# Define schemas
conversations_schema = """
    conversation_id VARCHAR(36) PRIMARY KEY,
    conversation JSON,
    summary TEXT
"""
tags_schema = """
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    conversation_id VARCHAR(36) UNIQUE,
    sentiment JSON,
    emotion JSON,
    topic VARCHAR(255),
    FOREIGN KEY (conversation_id) REFERENCES Conversations(conversation_id) ON DELETE CASCADE
"""

# Create necessary tables
db = MySQLConnection()
db.connect_to_database('rag')
db.create_table('Conversations', conversations_schema)
db.create_table('Tags', tags_schema)

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
    "summary": "Traffic stop for running a red light"
}

tag_data = {
    "conversation_id": "f98aa0a2-d461-431b-a8a2-efefba16f142",
    "sentiment": json.dumps({
        "Person A": "apologetic",
        "Person B": "authoritative"
    }),
    "emotion": json.dumps({
        "Person A": ["confused", "apologetic"],
        "Person B": ["stern", "authoritative"]
    }),
    "topic": "Traffic violation"
}

db.insert_data('Conversations', conversation_data, primary_key='conversation_id')
db.insert_data('Tags', tag_data, primary_key='conversation_id')

def search_conversations(search_term):
    db = MySQLConnection()
    results = db.search_data('Conversations', search_term, ['summary'])
    return results

def search_tags_by_topic(topic):
    db = MySQLConnection()
    query = f"SELECT * FROM Tags WHERE topic LIKE %s"
    results = db.custom_query(query, [f"%{topic}%"])
    return results

# conditions = {"conversation_id": "f98aa0a2-d461-431b-a8a2-efefba16f142"}
# db.delete_data("Tags", conditions)
# db.read_data("Tags", conditions)

# data = {
#         "conversation_id": tag_data["conversation_id"],
#         "sentiment": json.dumps(tag_data["sentiment"]),  # Convert to JSON string
#         "emotion": json.dumps(tag_data["emotion"]),    # Convert to JSON string
#         "topic": tag_data["topic"]
#     }
# db.insert_data("Tags", data, primary_key="conversation_id")

def search_sentiment(table_name: str, person: str, sentiment_value: str):
    with self.connect_to_database(self.database) as conn:
        with conn.cursor() as cursor:
            query = f"""
                SELECT * FROM {table_name}
                WHERE JSON_UNQUOTE(JSON_EXTRACT(sentiment, '$."{person}"')) = %s
            """
            cursor.execute(query, (sentiment_value,))
            results = cursor.fetchall()
            return results

sentiment_results = db.search_sentiment('Tags', 'Person A', 'apologetic')
print(sentiment_results)

sentiment_search_results = db.search_person_in_sentiment('Tags', 'Person A')
print("Sentiment Search Results:")
for result in sentiment_search_results:
    print(result)


# def search_tags_by_emotion(emotion):
#     db = MySQLConnection()
#     # This query searches for any tag entry that contains the emotion anywhere in the emotion JSON array
#     query = f"SELECT * FROM Tags WHERE JSON_CONTAINS(emotion, '\"{emotion}\"')"
#     results = db.custom_query(query)
#     return results

# search_results = search_conversations('Traffic stop')
# print(search_results)

# topic_results = search_tags_by_topic('Traffic violation')
# print('Topic Search Results:', topic_results)

# sentiment_results = search_tags_by_sentiment('Person A', 'apologetic')
# print('Sentiment Search Results:', sentiment_results)