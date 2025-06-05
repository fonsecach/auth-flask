from flask import Flask
from infrastructure.database import db
from infrastructure.config import Config
from flask_login import LoginManager

import models
from models.user import User
from routes.register import register_blueprints

app = Flask(__name__)
app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'auth.login'

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=["GET"])
def root():
    return "Aplicação Flask com SQLAlchemy e Flask-Login!"

# Registrar blueprints
register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)