class Already_Exist_Task_Exception(Exception):
    
    def __init__(self, *args):
        super().__init__(*args)