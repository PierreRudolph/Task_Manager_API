import uuid
from extensions import db


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True,default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    tasks = db.relationship("Task", backref="user")


class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True,default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    category = db.Column(db.String(50))
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)