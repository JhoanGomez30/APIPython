import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname= "postgres",
            user= "postgres",
            password= "postgres",
            host= "localhost",
            port= "5432")
        
        cursor = connection.cursor()
        print("Successfully connected to the database")
        return connection, cursor
        
    except psycopg2.Error as e:
        return None, f"Error connecting to the database: {e}"
