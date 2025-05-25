from flask import Flask
from infrastructure.database import db
from infrastructure.config import Config

app = Flask(__name__)
app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI

db.init_app(app)
# Session <- conexão ativa


@app.route("/", methods=["GET"])
def hello_world():
    return "Aplicação Flask com SQLAlchemy e Flask-Login!"


if __name__ == "__main__":
    app.run(debug=True)
