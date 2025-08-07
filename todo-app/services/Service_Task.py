from repository.Repo_Task import Repo_Task
from models.Task import Task

class Service_Task:
    def __init__(self):
        self.repo = Repo_Task()

    def add_task(self, title, description):
        task = Task(title, description)
        self.repo.add_task(task)
        return task
    
    def get_task(self, task_id):
        return self.repo.get_task(task_id)

    def get_all_tasks(self):
        return self.repo.get_all_tasks()
    
    def update_task(self, id, task):
        self.repo.update_task(id, task)
    
    def delete_task(self, task_id):
        self.repo.delete_task(task_id)

    def delete_all_tasks(self):
        self.repo.delete_all()

    def complete_task(self, task_id):
        self.repo.complete_task(task_id)

        