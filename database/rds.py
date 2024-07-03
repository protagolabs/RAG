import os
import pymysql
from dotenv import load_dotenv
from typing import List, Dict, Any

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

    def create_database(self, database_name: str):
        with self.connect_to_database() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
                conn.commit()

    def list_databases(self) -> List[str]:
        with self.connect_to_database() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SHOW DATABASES")
                result = cursor.fetchall()
                return [row['Database'] for row in result]

    def delete_database(self, database_name: str):
        with self.connect_to_database() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")
                conn.commit()

    def create_table(self, table_name: str, schema: str):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()

    def list_tables(self) -> List[str]:
        query = "SHOW TABLES"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return [row[f'Tables_in_{self.database}'] for row in result]

    def describe_table(self, table_name: str) -> List[Dict[str, Any]]:
        query = f"DESCRIBE {table_name}"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result

    def delete_table(self, table_name: str):
        query = f"DROP TABLE IF EXISTS {table_name}"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()
    
    def insert_data(self, table_name: str, data: Dict[str, Any]):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, list(data.values()))
                conn.commit()

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

    def search_data(self, table_name: str, search_term: str, columns: List[str]) -> List[Dict[str, Any]]:
        like_clause = ' OR '.join([f"{col} LIKE %s" for col in columns])
        search_value = f"%{search_term}%"
        query = f"SELECT * FROM {table_name} WHERE {like_clause}"
        with self.connect_to_database(self.database) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [search_value] * len(columns))
                results = cursor.fetchall()
                return results if results else []

# Example usage
if __name__ == "__main__":
    rds = MySQLConnection()
    
    # Create a new database
    rds.create_database(rds.database)
    
    # List all existing databases
    databases = rds.list_databases()
    print("Databases:", databases)
    
    # Connect to the 'rag' database
    rds.connect_to_database(rds.database)

    # Define table schema and create users and relationships tables without foreign key constraints
    user_table_schema = """
        id INT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        full_name VARCHAR(255) NOT NULL,
        metadata TEXT
    """
    relationship_table_schema = """
        user_id INT,
        friend_id INT,
        relationship_type VARCHAR(50),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (friend_id) REFERENCES users(id),
        PRIMARY KEY (user_id, friend_id)
    """
    rds.create_table('users', user_table_schema)
    rds.create_table('relationships', relationship_table_schema)

    # list tables
    print(rds.list_tables())

    # describe tables
    print(rds.describe_table('relationships'))

    # Insert data into the users table
    user_data = [
        {"id": 1, "username": "john_doe", "email": "john@example.com", "full_name": "John Doe", "metadata": "user profile data"},
        {"id": 2, "username": "jane_smith", "email": "jane@example.com", "full_name": "Jane Smith", "metadata": "user profile data"}
    ]
    for user in user_data:
        rds.insert_data('users', user)
    
    # Insert data into the relationships table
    relationship_data = {
        "user_id": 1,
        "friend_id": 2,
        "relationship_type": "friend"
    }
    rds.insert_data('relationships', relationship_data)

    # Read data from the relationships table
    conditions = {"user_id": 1}
    user_relationships = rds.read_data('relationships', conditions)
    print("User Relationships:", user_relationships)

    # Update data in the relationships table
    updated_relationship_data = {
        "relationship_type": "best_friend"
    }
    rds.update_data('relationships', updated_relationship_data, conditions)

    # Read the updated relationships
    updated_user_relationships = rds.read_data('relationships', conditions)
    print("Updated User Relationships:", updated_user_relationships)

    # Delete data from the relationships table
    rds.delete_data('relationships', conditions)

    # Verify the relationship has been deleted
    deleted_relationship = rds.read_data('relationships', conditions)
    print("Deleted Relationship:", deleted_relationship)

    # Search for users based on a search term
    search_results = rds.search_data('users', "john", ["username", "email", "full_name", "metadata"])
    print("Search Results:", search_results)

    # Delete the relationships table
    rds.delete_table('relationships')
    
    # Verify the table has been deleted
    tables_after_deletion = rds.list_tables()
    print("Tables after deletion:", tables_after_deletion)
