import mysql.connector

def connect_to_database():
    try:
        print("Connecting to MySQL database...")
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="crup_app"
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def close_database_connection(connection, cursor):
    try:
        cursor.close()
        connection.close()
    except mysql.connector.Error as e:
        print(f"Error closing database connection: {e}")