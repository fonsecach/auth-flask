from flask import Flask, jsonify, request
from infrastructure.database import db
from infrastructure.config import Config
from flask_login import LoginManager, login_user, current_user

import models
from models.user import User

app = Flask(__name__)
app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

#view
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:

        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({'message': 'Autenticacao realizada com sucesso!'})
        
    return jsonify({"message": "Credenciais invalidas!"}), 400


@app.route("/", methods=["GET"])
def root():
    return "Aplicação Flask com SQLAlchemy e Flask-Login!"


if __name__ == "__main__":
    app.run(debug=True)
