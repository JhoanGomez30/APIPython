class Task_Not_Found_Exception(Exception):
    
    def __init__(self, *args):
        super().__init__(*args)