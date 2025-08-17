from services.Service_Task import Service_Task
from models.Task import Task
from flask import Blueprint, jsonify, request
from exceptions.Already_Exist_Task_Exception import Already_Exist_Task_Exception
from exceptions.Task_Not_Found_Exception import Task_Not_Found_Exception
from exceptions.Task_Already_Completed import Task_Already_Completed
from exceptions.Task_Already_Incompleted import Task_Already_Incompleted


task_bp = Blueprint('task_bp', __name__)
services = Service_Task()

@task_bp.route('/addTask', methods=["POST"])
def add_task():
    data = request.get_json()

    task = services.add_task(**data)
    return jsonify({ 
        "message": "Task created successfully",
        "data": task.to_dict()
    }), 201

@task_bp.route("/tasks", methods=["GET"])
def get_all_tasks():    
    tasks = services.get_all_tasks()

    return jsonify({
        "message": "All tasks", 
        "data":[t.to_dict() for t in tasks]
    }), 200


@task_bp.route("/task/<int:id>", methods=["GET"])
def get_task(id):
    task = services.get_task(id)

    return jsonify({
        "message": "Task found",
        "data": task.to_dict()
    }),200

@task_bp.route("/update-task/<int:id>", methods=["PUT"])
def update_task(id):
    
    data = request.get_json()
    task = Task(**data)
    updated = services.update_task(id, task)

    return jsonify({
        "message": "task updated",
        "data" : updated.to_dict()
    }), 200
    


@task_bp.route("/delete-task/<int:id>", methods=["DELETE"])
def delete_task(id):
    

    is_delete = services.delete_task(id)

    return jsonify({
        "message": "Deleted task",
        "state": is_delete
    }),200
    
@task_bp.route("/delete-all", methods=["DELETE"])
def delete_all_tasks():
    is_delete = services.delete_all_tasks()

    return jsonify({
        "message": "Deleted tasks",
        "state": is_delete
    }),200

@task_bp.route("/complete-task/<int:id>", methods=["PUT"])
def complete_task(id):

    task = services.complete_task(id)

    return jsonify({
        "message": "Task has been Completed",
        "data": task.to_dict()
    }),201
    

@task_bp.route("/incomplete-task/<int:id>", methods=["PUT"])
def to_make_incomplete_task(id):
    
    task = services.to_make_incomplete_task(id)
    return jsonify({
        "message": "Task has been make incompleted",
        "data": task.to_dict()
    }),201

@task_bp.route("/search-title/<string:title>", methods=["GET"])
def search_by_title(title):

    task = services.search_by_title(title)

    return jsonify({
        "message": "task found",
        "data": [t.to_dict() for t in task]
    }), 200

