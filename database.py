import psycopg2

def connect_to_database():
   try:
       conn = psycopg2.connect(
           host="localhost",
           database="postgres",
           user="postgres",
           password="postgres",
           port="5432" 
       )
       print("Conexión exitosa a la base de datos")
       cursor = conn.cursor()
       return conn, cursor

   except psycopg2.Error as e:
       print(f"Error al conectar a la base de datos: {e}")

conn, cursor = connect_to_database()

def create_table():
    conn, cursor = connect_to_database()
    if conn:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INTEGER
            )
        """)
        conn.commit()
        print("Tabla creada exitosamente")
    else:
        print("No se pudo crear la tabla, conexión fallida")


def insert_user():

    cursor.execute('''INSERT INTO users (name, age) VALUES (%s, %s)''', ("Ana Lopez", 28))
    conn.commit()


def get_users():
    cursor.execute("SELECT * FROM users")
    usuarios = cursor.fetchall()  # Devuelve una lista de tuplas
    for usuario in usuarios:
        print(usuario)

def close_connection():
    if conn:
        conn.close()
        print("Conexión cerrada")
    else:
        print("No hay conexión para cerrar")


create_table()
insert_user()
get_users()
close_connection()