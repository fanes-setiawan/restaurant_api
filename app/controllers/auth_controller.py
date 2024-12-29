from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from app.models.user import User
from datetime import timedelta
from config import db

def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id , expires_delta=timedelta(hours=12))
        response = {
            "access_token": access_token,
            "role": user.role,
        }
        return jsonify(response), 200
    return jsonify({"msg": "Bad username or password"}), 401

def register_user():
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')
    
    print(username, password, role)

    if not username or not password or not role:
        return jsonify({"msg": "Missing required fields"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password, role=role)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User created successfully", "id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Failed to create user", "error": str(e)}), 500
