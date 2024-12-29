from werkzeug.security import generate_password_hash, check_password_hash
from config import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))
    role = db.Column(db.Enum('admin', 'customer'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def to_dict(self):
        """
        Convert the User object to a dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'createdAt': self.created_at,
        }
    
