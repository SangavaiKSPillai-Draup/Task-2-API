from functools import wraps
from Models.model import Customer
from flask_jwt_extended import get_jwt_identity
import json


def roles_required(roles):
    def decorator_role(f):
        @wraps(f)
        def wrapper_role(*args, **kwargs):
            user_id = get_jwt_identity()
            user = Customer.objects.get(_id=user_id).to_json()
            user1 = json.loads(user)
            user_role = user1['role']
            if user_role in roles:
                return f(*args, **kwargs)
            str1 = ", ".join(roles)
            str2 = "The following roles are accepted: " + str1
            return {"error": str2}, 500

        return wrapper_role

    return decorator_role
