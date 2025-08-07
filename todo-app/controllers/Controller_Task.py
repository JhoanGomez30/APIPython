from services.Service_Task import Service_Task
from flask import Blueprint, jsonify, request


    # def __init__(self, service_task):
    #     self.service_task = service_task

    # @app.route('/taks')
    # def get_users():
    #     return "1"

task_bp = Blueprint('task_bp', __name__)
services = Service_Task()

@task_bp.route('/addTask', methods=["POST"])
def add_task():
    data = request.get_json()
    task = services.add_task(**data)
    return jsonify(task.to_dict()), 201

@task_bp.route("/tasks", methods=["GET"])
def get_all_tasks():
    tareas = services.get_all_tasks()
    return jsonify([t.to_dict() for t in tareas])