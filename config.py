import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="",    # change if needed
        database="library_db"
    )
