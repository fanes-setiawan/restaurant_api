
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
# CORS(app,resources={r"/api/*": {"origins": "*"}},supports_credentials=True)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

Swagger(app, template_file="swagger.yaml")

@app.before_request
def handle_options_request():
    if request.method == "OPTIONS":
        response = app.response_class()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://secret123:2wsx1qaz@localhost:3306/restaurant_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://restaurantDb_poempushso:43190d57091ee0e83816925851d9c3b6fdae540b@ie3ct.h.filess.io:3306/restaurantDb_poempushso'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '2wsx1qaz' 

db = SQLAlchemy(app)
# db.init_app(app)

@app.route('/')
def home():
    return "21.83.0627 Fanes Setiawan"

app.app_context().push()
