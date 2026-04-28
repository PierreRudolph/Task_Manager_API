from flask import Blueprint, request, jsonify
from flask_jwt_extended import  create_access_token
from extensions import db

from models import User

auth_bp = Blueprint("auth","__name__")


# --REGISTER
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # einfache Validierung
    if not username or not password:
        return jsonify({"error": "Nutzername und Passwort sind Pflicht"}), 400

    # prüfen ob User existiert
    user_exist = User.query.filter_by(username=username).first()
    if (user_exist):
        return jsonify({"error": "Nutzer Existiert bereits"}), 400

    # neuen User anlegen
    new_user = User(username=username, password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Nutzer angelegt"}), 201

# --LOGIN


@auth_bp.route("/login", methods=["GET"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # User suchen
    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        return jsonify({"error": "Ungültige Login-Daten"}), 401

    # Token erstellen
    access_token = create_access_token(identity=str(user.id))

    return jsonify({"access_token": access_token}), 200