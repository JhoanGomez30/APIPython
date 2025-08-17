from flask import jsonify
from exceptions.Already_Exist_Task_Exception import Already_Exist_Task_Exception
from exceptions.Task_Already_Completed import Task_Already_Completed
from exceptions.Task_Already_Incompleted import Task_Already_Incompleted
from exceptions.Task_Not_Found_Exception import Task_Not_Found_Exception

def register_error_handlers(app):

    @app.errorhandler(Task_Not_Found_Exception)
    def handle_task_not_found(e):
        return jsonify({
            "error": "Tasks not found",
            "message": str(e)
        }), 404
    
    @app.errorhandler(Already_Exist_Task_Exception)
    def handle_already_exist_task(e):
        return jsonify({
            "error": "task already exist",
            "message": str(e)
        }),409
    
    @app.errorhandler(Task_Already_Completed)
    def handle_task_already_completed(e):
        return jsonify({
            "error": "Task already completed",
            "message": str(e)
        }),400
    
    @app.errorhandler(Task_Already_Incompleted)
    def handle_task_already_incompleted(e):
        return jsonify({
            "error": "Task already incompleted",
            "message": str(e)
        }),400
    
    @app.errorhandler(Exception)
    def handle_Exception(e):
        return jsonify({
            "error":"Server error",
            "message": str(e)
        }), 500
    
    @app.errorhandler(ValueError)
    def handle_ValueError(e):
        return jsonify({
            "error": "Validation error",
            "message": str(e)
        }),400
    
