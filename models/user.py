from app import db


class User(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(80), nullable=False, unique=True)
      email = db.Column(db.String(148), nullable=False, unique=True)
      password = db.Column(db.String(80), nullable=False)
      created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
      
