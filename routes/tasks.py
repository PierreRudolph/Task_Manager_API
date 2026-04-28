from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User, Task
from extensions import db

tasks_bp = Blueprint("tasks","__name__")


@tasks_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_Task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    category = data.get("category")
    user_id = data.get("user_id")

    # einfache Validierung
    if not title or title.strip() == "":
        return jsonify({"error": "Title ist Pflicht"}), 400

    # aktuellen User anlegen
    user_id = get_jwt_identity()

    # Task erstellen
    new_task = Task(
        title=title,
        description=description,
        category=category,
        user_id=int(user_id)
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Aufgabe angelegt"}), 201



@tasks_bp.route("/get_tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=int(user_id)).all()

    result = []
    for task in tasks:
        result.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "category": task.category,
            "completed": task.completed
        })

    return jsonify(result), 200


@tasks_bp.route("/get_tasks/<int:task_id>", methods=["GET"])
@jwt_required()
def get_task(task_id):
    user_id = get_jwt_identity()

    task = Task.query.get(task_id)

    # Task existiert nicht
    if not task:
        return jsonify({"error": "Task nicht gefunden"}), 404

    # Task gehört nicht diesem User
    if task.user_id != int(user_id):
        return jsonify({"error": "Kein Zugriff"}), 403

    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "category": task.category,
        "completed": task.completed
    }), 200
