from database.connection import SessionLocal
from repository.Repo_Task import Repo_Task
from models.Task import Task
from typing import List, Optional
from exceptions.Already_Exist_Task_Exception import Already_Exist_Task_Exception #, Task_Not_Found_Exception
from exceptions.Task_Not_Found_Exception import Task_Not_Found_Exception
from exceptions.Task_Already_Completed import Task_Already_Completed
from exceptions.Task_Already_Incompleted import Task_Already_Incompleted
class Service_Task:
    def __init__(self):
        self.db = SessionLocal()
        self.repo = Repo_Task(self.db)

    def __del__(self):
        self.db.close()

    def add_task(self, title: str, description: str, completed:bool = False) -> Task:
        
        if not isinstance(title, str) or not isinstance(completed, bool):
            raise ValueError("Title and description should be a string and completed a boolean")

        if(title is None or title.strip() == ""):
            raise ValueError ("Title cannot be empty")
        try:
            verify_existing = self.search_by_title(title)

            if(verify_existing):
                raise Already_Exist_Task_Exception("There are a task with that title")
            
        except Task_Not_Found_Exception:
        
            task = Task(title, description, completed)
            return self.repo.add_task(task)
        
    def get_task(self, task_id) -> Task:
            
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError ("Id task must be a number and greater than 0 ")

        task = self.repo.get_task(task_id)
        
        if not task:
            raise Task_Not_Found_Exception(f"Task with id {task_id} not found")
        return task

    def get_all_tasks(self):
        tasks = self.repo.get_all_tasks()
        if not tasks:
            raise Task_Not_Found_Exception("There are no tasks created yet")
        return tasks
    
    def update_task(self, id, task):

        try:
            task_to_update = self.get_task(id)
            existing_tasks = self.search_by_title(task.title)[0]
        
            if not (existing_tasks.id == task_to_update.id):
                raise Already_Exist_Task_Exception("Already exist another task with that title")
        
            return self.repo.update_task(id, task)
        except Task_Not_Found_Exception:
            return self.repo.update_task(id, task)
    
    def delete_task(self, task_id):
        self.get_task(task_id)
        return self.repo.delete_task(task_id)

    def delete_all_tasks(self):

        tasks = self.get_all_tasks()

        if not tasks:
            raise Task_Not_Found_Exception("There are no tasks to delete")
        
        return self.repo.delete_all_tasks()

    def complete_task(self, task_id) -> Optional[Task]:
        
        task = self.get_task(task_id)
        if task.completed:
            raise Task_Already_Completed("Task is already completed")
        
        return self.repo.complete_task(task_id)

    def to_make_incomplete_task(self, task_id) -> Optional[Task]:
        task = self.get_task(task_id)

        if not task.completed:
            raise Task_Already_Incompleted("Task is already decompleted")
        
        return self.repo.to_make_incomplete_task(task_id)

    def search_by_title(self, title) -> List[Task]:

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a string and not be empty")

        tasks = self.repo.search_tasks_by_title(title)

        if not tasks:
            raise Task_Not_Found_Exception("Tasks not found with that title")

        return tasks