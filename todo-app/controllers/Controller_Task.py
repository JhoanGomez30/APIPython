from services.Service_Task import Service_Task
from models.Task import Task
from flask import Blueprint, jsonify, request
from exceptions.Already_Exist_Task_Exception import Already_Exist_Task_Exception
from exceptions.Task_Not_Found_Exception import Task_Not_Found_Exception
from exceptions.Task_Already_Completed import Task_Already_Completed
from exceptions.Task_Already_Decompleted import Task_Already_Decompleted


task_bp = Blueprint('task_bp', __name__)
services = Service_Task()

@task_bp.route('/addTask', methods=["POST"])
def add_task():
    data = request.get_json()

    try:
        task = services.add_task(**data)
        return jsonify({ 
            "message": "Task created successfully",
            "data": task.to_dict()
        }), 201

    except Already_Exist_Task_Exception as aet:
        return jsonify({
            "error": str(aet)
        }),409
    except ValueError as ve:
        return jsonify({
            "error": "Validation error",
            "message": str(ve)
        }),409
    
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500    

    # task = services.add_task(**data)
    # return jsonify(task.to_dict()), 201

@task_bp.route("/tasks", methods=["GET"])
def get_all_tasks():
    
    try:
        tasks = services.get_all_tasks()

        if not tasks:
            return jsonify({
                "message": "There are no tasks created yet"
            }), 200

        return jsonify({
            "message": "All tasks", 
            "data":[t.to_dict() for t in tasks]
        }), 200
    
    except Task_Not_Found_Exception as tnf:
        return jsonify({
            "error": "Tasks not found ",
            "message": str(tnf)
        }), 400
    
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500


@task_bp.route("/task/<int:id>", methods=["GET"])
def get_task(id):
    try:
        task = services.get_task(id)

        return jsonify({
            "message": "Task found",
            "data": task.to_dict()
        }),200
    
    except Task_Not_Found_Exception as tnf:
        return jsonify({
            "error":"Task not found",
            "message": str(tnf)
        }), 404
    
    except ValueError as ve:
        return jsonify({
            "error": "Validation error",
            "message": str(ve)
        }), 400
    
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500

@task_bp.route("/update-task/<int:id>", methods=["PUT"])
def update_task(id):
    
    try:
        data = request.get_json()
        task = Task(**data)
        updated = services.update_task(id, task)

        return jsonify({
            "message": "task updated",
            "data" : updated.to_dict()
        }), 200
    
    except Already_Exist_Task_Exception as aet:
        return jsonify({
            "error": str(aet)
        }),409
    
    except Task_Not_Found_Exception as tnf:
        return jsonify({
            "error":"Task not found",
            "message": str(tnf)
        }), 404
    
    except Exception as e:
        return jsonify({
            "error":"Server error",
            "message": str(e)
        }), 500


@task_bp.route("/delete-task/<int:id>", methods=["DELETE"])
def delete_task(id):
    

    try:
        is_delete = services.delete_task(id)

        return jsonify({
            "message": "Task delete",
            "state": is_delete
        }),200
    
    except Task_Not_Found_Exception as tnf:
        return jsonify({
            "error":"Task not found",
            "message": str(tnf)
        }), 404
    
    except ValueError as ve:
        return jsonify({
            "error": "Validation error",
            "message": str(ve)
        }), 400
    
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500

@task_bp.route("/delete-all", methods=["DELETE"])
def delete_all_tasks():
    try:
        services.delete_all_tasks()

        return jsonify({
            "message": "Tasks deletes"
        }),200
    
    except Task_Not_Found_Exception as tnf:
        return jsonify({
            "error":"There are no Tasks to delete",
            "message": str(tnf)
        }), 404
    
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500

@task_bp.route("/complete-task/<int:id>", methods=["PUT"])
def complete_task(id):

    try:
        task = services.complete_task(id)

        return jsonify({
            "message": "Task has been Completed",
            "data": task.to_dict()
        }),201
    
    except Task_Not_Found_Exception as tnf:
        return jsonify({
            "error":"Task not found",
            "message": str(tnf)
        }), 404
    
    except Task_Already_Completed as aet:
        return jsonify({
            "error": str(aet)
        }),400
    
    except ValueError as ve:
        return jsonify({
            "error": "Validation error",
            "message": str(ve)
        }), 400
    
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500

@task_bp.route("/decomplete-task/<int:id>", methods=["PUT"])
def decomplete_task(id):
    try:
        task = services.decomplete_task(id)

        return jsonify({
            "message": "Task has been decompleted",
            "data": task.to_dict()
        }),201
    
    except Task_Not_Found_Exception as tnf:
        return jsonify({
            "error":"Task not found",
            "message": str(tnf)
        }), 404
    
    except ValueError as ve:
        return jsonify({
            "error": "Validation error",
            "message": str(ve)
        }), 400
    
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500

@task_bp.route("/search-title/<string:title>", methods=["GET"])
def search_by_title(title):

    try:
        # if not title.strip():
        #     return jsonify({"error": "El titulo no puede estar vacio"}), 400
        
        task = services.search_by_title(title)

        return jsonify({
            "message": "task found",
            "data": [t.to_dict() for t in task]
        }), 200
    except Task_Not_Found_Exception as tnf:
        return jsonify({
            "error":"Tasks not found",
            "message": str(tnf)
        }), 404
    except ValueError as ve:
        return jsonify({
            "error": "Validation error",
            "message": str(ve)
        }), 400
    except Exception as e:
        return jsonify({"error":str(e)}), 500

