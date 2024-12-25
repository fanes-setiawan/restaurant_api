
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://secret123:2wsx1qaz@localhost:3306/restaurant_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '2wsx1qaz' 

db = SQLAlchemy()
db.init_app(app)

@app.route('/')
def home():
    return "21.83.0627 Fanes Setiawan"

app.app_context().push()