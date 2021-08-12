from flask_restful import Resource
from Models.model import Smartphone
from flask import Response, request


class SmartphoneApi(Resource):
    def get(self):
        phones = Smartphone.objects.to_json()
        return Response(phones, mimetype='application/json', status=200)

    def post(self):
        # print(request)
        body = request.get_json()
        # print(body)
        phone = Smartphone(**body).save()
        id1 = phone.id
        return {'id': str(id1)}, 200
