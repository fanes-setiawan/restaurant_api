from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.models.user import User
from config import db
from werkzeug.security import generate_password_hash, check_password_hash

def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

def get_all_users():
    users = User.query.all()
    print(users)
    response={
        "users": [user.to_dict() for user in users],
        "count": len(users),
        "message": "Success"
    }
    return jsonify(response), 200

def get_user_by_id(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

def create_user():
    data = request.json
    if not data or 'username' not in data or 'password' not in data or 'role' not in data:
        return jsonify({"msg": "Missing required fields"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "Username already exists"}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'], password=hashed_password, role=data['role'])
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully", "id": new_user.id}), 201

def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json

    if 'username' in data:
        if User.query.filter_by(username=data['username']).first() and data['username'] != user.username:
            return jsonify({"msg": "Username already exists"}), 400
        user.username = data['username']
    
    if 'password' in data:
        user.password = generate_password_hash(data['password'])
    
    if 'role' in data:
        user.role = data['role']
    user.updated_at = db.func.now()

    db.session.commit()
    return jsonify({"msg": "User updated successfully"}), 200

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "User deleted successfully"}), 200

#delete_user >=1 by id
def delete_user_by_id(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "User deleted successfully"}), 200

def get_current_user():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"msg": "User not found"}), 404
