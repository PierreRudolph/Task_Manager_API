from routes.auth import auth_bp
from routes.tasks import tasks_bp
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db, limiter
from datetime import timedelta
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)
db.init_app(app)
limiter.init_app(app)
CORS(app, origins=["http://127.0.0.1:5000"])


# --HOME
app.register_blueprint(tasks_bp)
app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return "<p>Hello, World!</p>"


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
