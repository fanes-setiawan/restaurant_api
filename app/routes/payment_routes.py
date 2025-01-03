from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.payment_controller import (
    create_payment, get_payment_details, get_all_payments, get_payments_by_order,delete_payment
)

payment_bp = Blueprint('payment', __name__)

payment_bp.route('/api/payments', methods=['POST'])(jwt_required()(create_payment))
payment_bp.route('/api/payments/<int:payment_id>', methods=['GET'])(jwt_required()(get_payment_details))
payment_bp.route('/api/payments', methods=['GET'])(jwt_required()(get_all_payments))
payment_bp.route('/api/orders/<int:order_id>/payments', methods=['GET'])(jwt_required()(get_payments_by_order))
payment_bp.route('/api/payments/<int:payment_id>', methods=['DELETE'])(jwt_required()(delete_payment))
