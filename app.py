from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)
db.init_app(app)


# --HOME
from routes.tasks import tasks_bp
from routes.auth import auth_bp
app.register_blueprint(tasks_bp)
app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return "<p>Hello, World!</p>"


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
