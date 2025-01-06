from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify
from app.models.user import User


def role_required(required_role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):

            myId = get_jwt_identity()
            user = User.query.filter_by(id=myId).first()

            if user is None:
                return jsonify({"msg": "User not found"}), 404

            if user.role != required_role:
                return (
                    jsonify(
                        {"msg": "You do not have permission to access this resource"}
                    ),
                    403,
                )

            return fn(*args, **kwargs)

        return wrapper

    return decorator
