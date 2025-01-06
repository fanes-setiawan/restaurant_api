from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.role_required import role_required
from app.controllers.order_controller import (
    get_all_orders, create_order, get_order_details, update_order_status,
    add_order_item, update_order_item, delete_order_item, delete_order
)

order_bp = Blueprint('order', __name__)

order_bp.route('/api/orders', methods=['GET'])(jwt_required()(role_required('admin')(get_all_orders)))
order_bp.route('/api/orders', methods=['POST'])(jwt_required()(create_order))
order_bp.route('/api/orders/<int:order_id>', methods=['GET'])(jwt_required()(get_order_details))
order_bp.route('/api/orders/<int:order_id>', methods=['PUT'])(jwt_required()(role_required('admin')(update_order_status)))
order_bp.route('/api/orders/<int:order_id>', methods=['DELETE'])(jwt_required()(delete_order))
order_bp.route('/api/orders/<int:order_id>/items', methods=['POST'])(jwt_required()(add_order_item))
order_bp.route('/api/orders/<int:order_id>/items/<int:item_id>', methods=['PUT'])(jwt_required()(role_required('admin')(update_order_item)))
order_bp.route('/api/orders/<int:order_id>/items/<int:item_id>', methods=['DELETE'])(jwt_required()(delete_order_item))
