# FILEPATH: /Users/macbookpro/Documents/SEMESTER 7/restaurant_api/app/controllers/payment_controller.py

from flask import jsonify, request
from app.models.payment import Payment
from app.models.order import Order
from config import db
from datetime import datetime

def create_payment():
    data = request.json
    order = Order.query.get_or_404(data['order_id'])
    
    # Check if the order has already been paid
    if order.status == 'paid':
        return jsonify({"error": "This order has already been paid"}), 400
    
    new_payment = Payment(
        order_id=data['order_id'],
        amount=data['amount'],
        payment_method=data['payment_method'],
        payment_date=datetime.utcnow()
    )
    
    # Update order status to 'paid'
    order.status = 'paid'
    
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({
        "msg": "Payment recorded successfully",
        "payment_id": new_payment.id,
        "order_id": new_payment.order_id,
        "amount": float(new_payment.amount),
        "payment_method": new_payment.payment_method,
        "payment_date": new_payment.payment_date.isoformat()
    }), 201

def get_payment_details(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    return jsonify({
        "id": payment.id,
        "order_id": payment.order_id,
        "amount": float(payment.amount),
        "payment_method": payment.payment_method,
        "payment_date": payment.payment_date.isoformat()
    }), 200

def get_all_payments():
    payments = Payment.query.all()
    return jsonify([{
        "id": payment.id,
        "order_id": payment.order_id,
        "amount": float(payment.amount),
        "payment_method": payment.payment_method,
        "payment_date": payment.payment_date.isoformat()
    } for payment in payments]), 200

def get_payments_by_order(order_id):
    payments = Payment.query.filter_by(order_id=order_id).all()
    if not payments:
        return jsonify({"error": "No payments found for this order"}), 404
    
    return jsonify([{
        "id": payment.id,
        "order_id": payment.order_id,
        "amount": float(payment.amount),
        "payment_method": payment.payment_method,
        "payment_date": payment.payment_date.isoformat()
    } for payment in payments]), 200
    
def delete_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({"msg": "Payment deleted successfully"}), 200
