from flask import Blueprint
from app.controllers.role_required import role_required
from flask_jwt_extended import jwt_required
from app.controllers.user_controller import get_all_users, create_user, update_user, delete_user , get_user_by_id

user_bp = Blueprint('user', __name__)

user_bp.route('/api/users', methods=['GET'])(jwt_required()(role_required('admin')(get_all_users)))
user_bp.route('/api/users/<int:user_id>', methods=['GET'])(jwt_required()(get_user_by_id))
user_bp.route('/api/users', methods=['POST'])(jwt_required()(create_user))
user_bp.route('/api/users/<int:user_id>', methods=['PUT'])(jwt_required()(update_user))
user_bp.route('/api/users/<int:user_id>', methods=['DELETE'])(jwt_required()(role_required('admin')(delete_user)))
