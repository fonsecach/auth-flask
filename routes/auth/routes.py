import bcrypt
from flask import Blueprint, jsonify, request
from flask_login import login_user, current_user, logout_user, login_required
from models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)) == True:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({'message': 'Autenticacao realizada com sucesso!'})
        
    return jsonify({"message": "Credenciais invalidas!"}), 400

@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'Logout realizado com sucesso!'})
    return jsonify({'message': 'Nenhum usuario autenticado!'}), 400
