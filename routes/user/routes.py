import bcrypt
from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from infrastructure.database import db
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt(12))
        user = User(username=username, password=hashed_password, role="user")
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuario criado com sucesso!'})
    
    return jsonify({"message": "Usuario ja existente ou credenciais invalidas!"}), 400

@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    if not users:
        return jsonify({"message": "Nenhum usuário encontrado!"}), 404

    return jsonify([{"id": user.id, "username": user.username} for user in users]), 200




@user_bp.route("/<int:user_id>", methods=["GET"])
@login_required
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"username": user.username})
    return jsonify({"message": "Usuario nao encontrado!"}), 404

@user_bp.route("/<int:user_id>", methods=["PUT"])
@login_required
def update_user(user_id):
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if user_id != current_user.id and current_user.role!= "admin":
        return jsonify({"message": "Acesso restrito para administradores!"}), 403
    
    if username and password:
        user = User.query.get(user_id)
        if user:
            user.password = password
            db.session.commit()
            return jsonify({'message': f'Usuario com id {user_id} atualizado com sucesso!'})
        return jsonify({"message": "Usuario nao encontrado!"}), 404
    return jsonify({"message": "Credenciais invalidas!"}), 400

@user_bp.route("/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    
    if current_user.role != "admin":
        return jsonify({"message": "Acesso restrito para administradores!"}), 403
    
    if user and current_user.id != user_id:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'Usuario com id {user_id} deletado com sucesso!'})
    return jsonify({"message": "Usuario nao encontrado!"}), 404
