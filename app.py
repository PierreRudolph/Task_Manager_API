from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"]="super-secret-key"
jwt=JWTManager(app)
db = SQLAlchemy(app)


# --HOME
from models import User, Task


@app.route("/")
def home():
    return "<p>Hello, World!</p>"


# --REGISTER
@app.route("/register", methods=["POST"])
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



# --ADD NEW TASK
@app.route("/new_task", methods=["POST"])
def addTask():
    data = request.get_json()
    title = data.get("title")
    user_id = data.get("user_id")

    # einfache Validierung
    if not title or not user_id:
        return jsonify({"error": "Title und Passwort sind Pflicht"}), 400

    # neuen User anlegen
    new_task = Task(title=title, user_id=user_id)

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Aufgabe angelegt"}), 201


with app.app_context():
    db.create_all()


# --TEST
@app.route("/test-db")
def test_db():
    user = User(username="test1", password="1234")
    db.session.add(user)
    db.session.commit()
    return "<p>User erstellt</p>"


if __name__ == "__main__":
    app.run(debug=True)

# POST Methode
#  curl --json '{"username":"newTypeofPost","password":"newPassword"}' http://127.0.0.1:5000/register
#  curl --json '{"title":"newTypeofPost","user_id":"2342"}' http://127.0.0.1:5000/new_task
