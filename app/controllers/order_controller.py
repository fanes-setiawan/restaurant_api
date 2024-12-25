# FILEPATH: /Users/macbookpro/Documents/SEMESTER 7/restaurant_api/app/controllers/order_controller.py

from flask import jsonify, request
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.menu import Menu
from config import db

def get_all_orders():
    orders = Order.query.all()
    return jsonify([{
        'id': order.id,
        'user_id': order.user_id,
        'table_number': order.table_number,
        'status': order.status,
        'created_at': order.created_at.isoformat(),
        'updated_at': order.updated_at.isoformat(),
        'items': [{
            'id': item.id,
            'menu_id': item.menu_id,
            'menu_name': Menu.query.get(item.menu_id).name,
            'menu_price': Menu.query.get(item.menu_id).price*item.quantity,
            'quantity': item.quantity
        } for item in order.items]
    } for order in orders]), 200

def create_order():
    data = request.json
    new_order = Order(user_id=data['user_id'], table_number=data['table_number'])
    db.session.add(new_order)
    db.session.commit()
    menus = data['menu']
    for menu in menus:
        order_item = OrderItem(order_id=new_order.id, menu_id=menu["id"], quantity=menu['quantity'])
        db.session.add(order_item)
        db.session.commit()
        
    return jsonify({"msg": "Order created successfully", "id": new_order.id}), 201

def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.json
    order.status = data['status']
    db.session.commit()
    return jsonify({"msg": "Order status updated successfully"}), 200

def add_order_item(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.json
    new_item = OrderItem(order_id=order.id, menu_id=data['menu_id'], quantity=data['quantity'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"msg": "Order item added successfully", "id": new_item.id}), 201

def get_order_details(order_id):
    order = Order.query.get_or_404(order_id)
    order_items = OrderItem.query.filter_by(order_id=order_id).all()
    return jsonify({
        'id': order.id,
        'user_id': order.user_id,
        'table_number': order.table_number,
        'status': order.status,
        'created_at': order.created_at.isoformat(),
        'updated_at': order.updated_at.isoformat(),
        'items': [{
            'id': item.id,
            'menu_id': item.menu_id,
            'quantity': item.quantity
        } for item in order_items]
    }), 200

def update_order_item(order_id, item_id):
    order_item = OrderItem.query.filter_by(order_id=order_id, id=item_id).first_or_404()
    data = request.json
    order_item.quantity = data['quantity']
    db.session.commit()
    return jsonify({"msg": "Order item updated successfully"}), 200

def delete_order_item(order_id, item_id):
    order_item = OrderItem.query.filter_by(order_id=order_id, id=item_id).first_or_404()
    db.session.delete(order_item)
    db.session.commit()
    return jsonify({"msg": "Order item deleted successfully"}), 200

def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"msg": "Order deleted successfully"}), 200
