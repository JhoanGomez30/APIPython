import psycopg2
from models.Task import Task
from database.connection import connect_to_db

class Repo_Task:
    def __init__(self):
        self.connection, self.cursor = connect_to_db()
        if not self.connection:
            raise Exception("Failed to connect to the database")
        self.create_table()
        
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT FALSE
            )
        ''')
        self.connection.commit()

    def add_task(self, task):
        self.cursor.execute('''
            INSERT INTO tasks (title, description, completed)
            VALUES (%s, %s, %s)
        ''', (task.title, task.description, task.completed))
        self.connection.commit()
    
    def get_task(self, task_id):
        self.cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
        row = self.cursor.fetchone()
        if row:
            return Task(id=row[0], title=row[1], description=row[2], completed=row[3])
            # return Task(*row)
        return None

    def get_all_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        rows = self.cursor.fetchall()
        return [Task(id=row[0], title=row[1], description=row[2], completed=row[3]) for row in rows]   
    
    def update_task(self, id, task):
        self.cursor.execute('''
            UPDATE tasks SET title = %s, description = %s, completed = %s, id = %s
            WHERE id = %s
        ''', (task.title, task.description, task.completed, task.id, id))
        self.connection.commit()
    
    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
        self.connection.commit()
    
    def delete_all(self):
        self.cursor.execute('DELETE FROM tasks')
        self.connection.commit()
        return

    def complete_task(self, task_id):
        self.cursor.execute('UPDATE tasks SET completed = TRUE WHERE id = %s', (task_id,))
        self.connection.commit()