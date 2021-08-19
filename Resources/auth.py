"""
    This file contains code to login/signup into the application.
"""

import datetime
from flask import request
from Models.model import Customer
from flask_restful import Resource
from flask_jwt_extended import create_access_token


class SignupApi(Resource):
    """
    Signup to application
    """
    def post(self):
        body = request.get_json()
        customer_instance = Customer(**body)
        customer_instance.hash_password()
        customer_instance.save()
        id = customer_instance.id
        return {'id': str(id)}, 200


class LoginApi(Resource):
    """
    Login to application
    """
    def post(self):
        body = request.get_json()
        user = Customer.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
