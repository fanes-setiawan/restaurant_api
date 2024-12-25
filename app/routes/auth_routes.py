from flask import Blueprint
from app.controllers.auth_controller import login ,register_user

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/api/login', methods=['POST'])(login)
auth_bp.route('/api/register', methods=['POST'])(register_user)

