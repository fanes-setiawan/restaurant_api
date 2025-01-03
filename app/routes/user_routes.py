# FILEPATH: /Users/macbookpro/Documents/SEMESTER 7/restaurant_api/app/routes/user_routes.py

from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.user_controller import get_all_users, create_user, update_user, delete_user , get_user_by_id

user_bp = Blueprint('user', __name__)

user_bp.route('/api/users', methods=['GET'])(jwt_required()(get_all_users))
user_bp.route('/api/users/<int:user_id>', methods=['GET'])(jwt_required()(get_user_by_id))
user_bp.route('/api/users', methods=['POST'])(jwt_required()(create_user))
user_bp.route('/api/users/<int:user_id>', methods=['PUT'])(jwt_required()(update_user))
user_bp.route('/api/users/<int:user_id>', methods=['DELETE'])(jwt_required()(delete_user))
