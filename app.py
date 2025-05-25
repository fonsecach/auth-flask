from flask import Flask
from infrastructure.database import db
from infrastructure.config import Config


import models

app = Flask(__name__)
app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def hello_world():
    return "Aplicação Flask com SQLAlchemy e Flask-Login!"


if __name__ == "__main__":
    app.run(debug=True)
