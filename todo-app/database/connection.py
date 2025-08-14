#CONEXION A BASE DE DATOS SIMPLE
# import psycopg2

# def connect_to_db():
#     try:
#         connection = psycopg2.connect(
#             user = "postgres",
#             dbname= "notingapp",
#             password= "postgres",
#             host= "localhost",
#             port= "5433")
        
#         cursor = connection.cursor()
#         print("Successfully connected to the database")
#         return connection, cursor
        
#     except psycopg2.Error as e:
#         return None, f"Error connecting to the database: {e}"


#CONEXION A BASE DE DATOS CON SQLAlquemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/notingapp"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()