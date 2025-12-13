import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database in MySQL server."""
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='5fr7g9D4vjfZBFGCf9w0'
        )
        
        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            # Close cursor
            cursor.close()
            
    except Error as e:
        # Print error message if connection fails
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        # Close the database connection
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()