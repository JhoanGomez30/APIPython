class Task_Already_Decompleted(Exception):
    def __init__(self, *args):
        super().__init__(*args)