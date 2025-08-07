class Task():
    def __init__(self, title, description, id=None, completed=False):
        self.id=id
        self.title = title
        self.description = description
        self.completed = completed
        
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
    
    def mark_completed(self, state):
        self.completed = state

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    def __str__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    @staticmethod
    def from_dict(data):
        return Task(
            id=data.get("id"),
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )