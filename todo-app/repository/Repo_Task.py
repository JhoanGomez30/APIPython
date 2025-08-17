
from models.Task import Task
from database.connection import get_db

from sqlalchemy.orm import Session
from models.Task import Task
from typing import List, Optional

class Repo_Task:
    # def __init__(self, db : Session):
    #     self.connection, self.cursor = connect_to_db()
    #     if not self.connection:
    #         raise Exception("Failed to connect to the database")
    #     self.create_table()
        
    # def create_table(self):
    #     self.cursor.execute('''
    #         CREATE TABLE IF NOT EXISTS tasks (
    #             id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    #             title VARCHAR(255) NOT NULL,
    #             description TEXT,
    #             completed BOOLEAN DEFAULT FALSE
    #         )
    #     ''')
    #     self.connection.commit()

    # def add_task(self, task):
    #     self.cursor.execute('''
    #         INSERT INTO tasks (title, description, completed)
    #         VALUES (%s, %s, %s)
    #     ''', (task.title, task.description, task.completed))
    #     self.connection.commit()
    
    # def get_task(self, task_id):
    #     self.cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
    #     row = self.cursor.fetchone()
    #     if row:
    #         return Task(id=row[0], title=row[1], description=row[2], completed=row[3])
    #         # return Task(*row)
    #     return None

    # def get_all_tasks(self):
    #     self.cursor.execute('SELECT * FROM tasks')
    #     rows = self.cursor.fetchall()
    #     return [Task(id=row[0], title=row[1], description=row[2], completed=row[3]) for row in rows]   
    
    # def update_task(self, id, task):
    #     self.cursor.execute('''
    #         UPDATE tasks SET title = %s, description = %s, completed = %s
    #         WHERE id = %s
    #     ''', (task.title, task.description, task.completed, id))
    #     self.connection.commit()
    
    # def delete_task(self, task_id):
    #     self.cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    #     self.connection.commit()
    
    # def delete_all(self):
    #     self.cursor.execute('DELETE FROM tasks')
    #     self.connection.commit()
    #     return

    # def complete_task(self, task_id):
    #     self.cursor.execute('UPDATE tasks SET completed = TRUE WHERE id = %s', (task_id,))
    #     self.connection.commit()

    # def decomplete_task(self, task_id):
    #     self.cursor.execute('UPDATE tasks SET completed = TRUE WHERE id = %s', (task_id,))

    # def search_task_by_title(self, title):
    #     self.cursor.execute()


    def __init__(self, db: Session):
        self.db = db

    def add_task(self, task: Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        if not task: raise Exception("Cant add the task to db")
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def get_all_tasks(self) -> List[Task]:
        return self.db.query(Task).all()

    def update_task(self, id: int, task_data: Task) -> Optional[Task]:
        db_task = self.get_task(id)
        if db_task:
            for key, value in task_data.to_dict().items():
                if key != "id":  # evitar modificar el ID
                    setattr(db_task, key, value)
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)

        if task:
            self.db.delete(task)
            self.db.commit()
            return True
        return False

    def delete_all_tasks(self):
        self.db.query(Task).delete()
        self.db.commit()
        return True

    def complete_task(self, task_id: int) -> Optional[Task]:
        task = self.get_task(task_id)
        if task:
            task.completed = True
            self.db.commit()
            self.db.refresh(task)
        return task
    
    def to_make_incomplete_task(self, task_id: int) -> Optional[Task]:
        task = self.get_task(task_id)
        if task:
            task.completed = False
            self.db.commit()
            self.db.refresh(task)
        return task

    def search_tasks_by_title(self, title: str) -> List[Task]:
        return self.db.query(Task).filter(Task.title.ilike(f"%{title}%")).all()