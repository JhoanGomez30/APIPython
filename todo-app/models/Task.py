from sqlalchemy import Column, Integer, String, Boolean
from database.connection import Base

class Task(Base):

    __tablename__ = "tasks"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

    def __init__(self, title, description, completed=False, id=None):
        self.id=id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self, included_id=True):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
        
    
        
    def __get_id__(self):
        return self.id
    
    def __get_title__(self):
        return self.title
    
    def __set_title__(self, title):
        self.title = title
    
    def __get_description__(self):
        return self.description
    
    def __set_description__(self, description):
        self.description = description
        
    def __get_completed__(self):
        return self.completed
    

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "title": self.title,
    #         "description": self.description,
    #         "completed": self.completed
    #     }

    # def __str__(self):
    #     return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    # @staticmethod
    # def from_dict(data):
    #     return Task(
    #         id=data.get("id"),
    #         title=data["title"],
    #         description=data.get("description"),
    #         completed=data.get("completed")
    #     )