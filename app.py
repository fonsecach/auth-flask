from flask import Flask, jsonify, request
from infrastructure.database import db
from infrastructure.config import Config
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

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
    return User.query.get(int(user_id))


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


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'Logout realizado com sucesso!'})
    return jsonify({'message': 'Nenhum usuario autenticado!'}), 400


@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuario criado com sucesso!'})
    
    return jsonify({"message": "Usuario ja existente ou credenciais invalidas!"}), 400


@app.route("/user/<int:user_id>", methods=["GET"])
@login_required
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"username": user.username})
    return jsonify({"message": "Usuario nao encontrado!"}), 404


@app.route("/user/<int:user_id>", methods=["PUT"])
@login_required
def update_user(user_id):
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        user = User.query.get(user_id)
        if user:
            user.password = password
            db.session.commit()
            return jsonify({'message': f'Usuario com id {user_id} atualizado com sucesso!'})
        return jsonify({"message": "Usuario nao encontrado!"}), 404
    return jsonify({"message": "Credenciais invalidas!"}), 400


@app.route("/user/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if user and current_user.id != user_id:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'Usuario com id {user_id} deletado com sucesso!'})
    return jsonify({"message": "Usuario nao encontrado!"}), 404


@app.route("/", methods=["GET"])
def root():
    return "Aplicação Flask com SQLAlchemy e Flask-Login!"


if __name__ == "__main__":
    app.run(debug=True)