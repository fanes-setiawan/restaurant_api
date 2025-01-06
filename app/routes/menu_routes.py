from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.role_required import role_required
from app.controllers.menu_controller import get_all_menus, create_menu, update_menu, delete_menu,get_menu_by_id

menu_bp = Blueprint('menu', __name__)

# Menu management routes
menu_bp.route('/api/menus', methods=['GET'])(jwt_required()(get_all_menus))
menu_bp.route('/api/menus', methods=['POST'])(jwt_required()(role_required('admin')(create_menu)))
menu_bp.route('/api/menus/<int:menu_id>', methods=['GET'])(jwt_required()(get_menu_by_id))
menu_bp.route('/api/menus/<int:menu_id>', methods=['PUT'])(jwt_required()(role_required('admin')(update_menu)))
menu_bp.route('/api/menus/<int:menu_id>', methods=['DELETE'])(jwt_required()(role_required('admin')(delete_menu)))
