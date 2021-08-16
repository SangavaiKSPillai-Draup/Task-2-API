import datetime
from flask import request
from Models.model import Customer
from flask_restful import Resource
from flask_jwt_extended import create_access_token


class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        cust = Customer(**body)
        cust.hash_password()
        cust.save()
        id = cust.id
        return {'id': str(id)}, 200


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = Customer.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
