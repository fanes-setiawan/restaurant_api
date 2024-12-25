from flask import jsonify, request
from app.models.menu import Menu
from config import db

def get_all_menus():
    menus = Menu.query.all()
    print(menus)
    response={
        "menus": [menu.to_dict() for menu in menus],
        "count": len(menus),
        "message": "Success"
    }
    return jsonify(response), 200

def create_menu():
    data = request.json
    image_url = data.get('image_url', None)
    new_menu = Menu(name=data['name'], description=data['description'], price=data['price'],image_url=image_url)
    db.session.add(new_menu)
    db.session.commit()
    return jsonify({"msg": "Menu item created successfully", "id": new_menu.id}), 201

def update_menu(menu_id):
    menu = Menu.query.get_or_404(menu_id)
    data = request.json
    menu.name = data.get('name', menu.name)
    menu.description = data.get('description', menu.description)
    menu.price = data.get('price', menu.price)
    db.session.commit()
    return jsonify({"msg": "Menu item updated successfully"}), 200

def delete_menu(menu_id):
    menu = Menu.query.get_or_404(menu_id)
    db.session.delete(menu)
    db.session.commit()
    return jsonify({"msg": "Menu item deleted successfully"}), 200
def get_menu_by_id(menu_id):
    menu = Menu.query.get_or_404(menu_id)
    return jsonify({
        'id': menu.id,
        'name': menu.name,
        'description': menu.description,
        'price': float(menu.price)
    }), 200
