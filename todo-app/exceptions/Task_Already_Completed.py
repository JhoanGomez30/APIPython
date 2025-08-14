class Task_Already_Completed(Exception):
    def __init__(self, *args):
        super().__init__(*args)