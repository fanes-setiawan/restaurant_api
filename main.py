from config import app, db
from flask_jwt_extended import JWTManager ,get_jwt_identity, jwt_required
from flask import request ,jsonify
from app.routes.auth_routes import auth_bp
from app.routes.menu_routes import menu_bp
from app.routes.order_routes import order_bp
from app.routes.payment_routes import payment_bp
from app.routes.user_routes import user_bp

app.register_blueprint(auth_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(user_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(order_bp)

jwt = JWTManager(app)

@app.before_request
def before_request():
    print("Before Request")
    excluded_routes = ['/api/login','/api/register']
    if request.path in excluded_routes:
        return None
    
@app.route('/api/protected',methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user),200

db.create_all()
if __name__ == '__main__':
    app.run(debug=True)