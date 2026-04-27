from app import db


class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # 👈 DAS ist Pflicht
        username = db.Column(db.String(80), unique=True, nullable=False)