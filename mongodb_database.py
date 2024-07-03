import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
from typing import List, Dict, Any

# Load environment variables
load_dotenv()

class MongoDBConnection:
    def __init__(self):
        self.config = {
            'host': os.getenv('MONGODB_HOST'),
            'port': int(os.getenv('MONGODB_PORT')),
            'username': os.getenv('MONGODB_USERNAME'),
            'password': os.getenv('MONGODB_PASSWORD')
        }
        self.database_name = os.getenv('MONGODB_DATABASE')
        self.client = None
        self.db = None

    def connect_to_server(self):
        try:
            self.client = MongoClient(
                host=self.config['host'],
                port=self.config['port'],
                username=self.config['username'],
                password=self.config['password']
            )
        except ConnectionFailure as e:
            print(f"Could not connect to MongoDB server: {e}")

    def create_database(self, database_name: str):
        self.connect_to_server()
        self.db = self.client[database_name]
        # Creating a collection to ensure database creation
        self.db.create_collection("init_collection")
        self.db.drop_collection("init_collection")
        print(f"Database '{database_name}' created or already exists.")

    def connect_to_database(self, database_name: str = None):
        self.connect_to_server()
        if not database_name:
            database_name = self.database_name
        self.db = self.client[database_name]

    def create_collection(self, collection_name: str):
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)

    def list_collections(self) -> List[str]:
        return self.db.list_collection_names()

    def delete_collection(self, collection_name: str):
        self.db.drop_collection(collection_name)

    def insert_document(self, collection_name: str, document: Dict[str, Any]):
        collection = self.db[collection_name]
        collection.insert_one(document)

    def insert_documents(self, collection_name: str, documents: List[Dict[str, Any]]):
        collection = self.db[collection_name]
        collection.insert_many(documents)

    def read_documents(self, collection_name: str, query: Dict[str, Any] = {}) -> List[Dict[str, Any]]:
        collection = self.db[collection_name]
        return list(collection.find(query))

    def update_documents(self, collection_name: str, query: Dict[str, Any], update: Dict[str, Any]):
        collection = self.db[collection_name]
        collection.update_many(query, {'$set': update})

    def delete_documents(self, collection_name: str, query: Dict[str, Any]):
        collection = self.db[collection_name]
        collection.delete_many(query)

    def search_documents(self, collection_name: str, search_term: str, fields: List[str]) -> List[Dict[str, Any]]:
        collection = self.db[collection_name]
        regex_query = {'$or': [{field: {'$regex': search_term, '$options': 'i'}} for field in fields]}
        return list(collection.find(regex_query))

    def create_index(self, collection_name: str, field_name: str):
        collection = self.db[collection_name]
        collection.create_index(field_name)
        print(f"Index created on field '{field_name}' in collection '{collection_name}'.")
    
    def text_search_documents(self, collection_name: str, search_term: str) -> List[Dict[str, Any]]:
        collection = self.db[collection_name]
        text_query = {'$text': {'$search': search_term}}
        return list(collection.find(text_query))

    def create_text_index(self, collection_name: str, fields: List[str]):
        collection = self.db[collection_name]
        index_fields = [(field, 'text') for field in fields]  # Create a list of tuples
        collection.create_index(index_fields)
        print(f"Text index created on fields {fields} in collection '{collection_name}'.")

# Example usage
if __name__ == "__main__":
    mongo_conn = MongoDBConnection()
    
    # Create and connect to the MongoDB database
    mongo_conn.create_database('rag')
    mongo_conn.connect_to_database('rag')
    
    # Create collections
    mongo_conn.create_collection('users')
    mongo_conn.create_collection('posts')
    mongo_conn.create_collection('comments')
    
    # List collections
    collections = mongo_conn.list_collections()
    print("Collections:", collections)
    
    # Insert documents into the 'users' collection
    user_data = [
        {"user_id": 1, "username": "john_doe", "email": "john@example.com", "full_name": "John Doe", "metadata": "user profile data"},
        {"user_id": 2, "username": "jane_smith", "email": "jane@example.com", "full_name": "Jane Smith", "metadata": "user profile data"}
    ]
    mongo_conn.insert_documents('users', user_data)
    
    # Insert documents into the 'posts' collection
    post_data = [
        {"post_id": 1, "user_id": 1, "content": "This is John's first post", "timestamp": "2024-07-03T10:00:00Z"},
        {"post_id": 2, "user_id": 2, "content": "This is Jane's first post", "timestamp": "2024-07-03T10:05:00Z"}
    ]
    mongo_conn.insert_documents('posts', post_data)
    
    # Insert documents into the 'comments' collection
    comment_data = [
        {"comment_id": 1, "post_id": 1, "user_id": 2, "content": "Great post, John!", "timestamp": "2024-07-03T10:10:00Z"},
        {"comment_id": 2, "post_id": 2, "user_id": 1, "content": "Thanks, Jane!", "timestamp": "2024-07-03T10:15:00Z"}
    ]
    mongo_conn.insert_documents('comments', comment_data)
    
    # Create indexes on 'comments' collection
    mongo_conn.create_index('comments', 'comment_id')
    mongo_conn.create_index('comments', 'post_id')
    mongo_conn.create_index('comments', 'user_id')
    
    # Read documents from the 'users' collection
    users = mongo_conn.read_documents('users')
    print("Users:", users)
    
    # Read documents from the 'posts' collection with a specific query
    user_posts = mongo_conn.read_documents('posts', {"user_id": 1})
    print("User Posts:", user_posts)
    
    # Update documents in the 'posts' collection
    mongo_conn.update_documents('posts', {"user_id": 1}, {"content": "This is John's updated post"})
    
    # Read the updated posts
    updated_posts = mongo_conn.read_documents('posts', {"user_id": 1})
    print("Updated Posts:", updated_posts)
    
    # Delete documents from the 'comments' collection
    mongo_conn.delete_documents('comments', {"comment_id": 1})
    
    # Verify the comment has been deleted
    comments_after_deletion = mongo_conn.read_documents('comments')
    print("Comments after deletion:", comments_after_deletion)
    
    # Create a text index on 'username', 'email', 'full_name', and 'metadata' fields
    mongo_conn.create_text_index('users', ['username', 'email', 'full_name', 'metadata'])
    
    # Perform a text search for 'john'
    search_results = mongo_conn.text_search_documents('users', "john")
    print("Search Results:", search_results)
    
    # Delete the 'posts' collection
    mongo_conn.delete_collection('posts')
    
    # Verify the collection has been deleted
    collections_after_deletion = mongo_conn.list_collections()
    print("Collections after deletion:", collections_after_deletion)
