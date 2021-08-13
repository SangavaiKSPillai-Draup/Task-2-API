from flask_restful import Resource
from Models.model import Smartphone, Customer, Orders
from flask import Response, request
import uuid


class SmartphoneApi(Resource):
    def get(self):
        phones = Smartphone.objects.to_json()
        return Response(phones, mimetype='application/json', status=200)

    def post(self):
        # print(request)
        body = request.get_json()
        # print(body)
        phone = Smartphone(**body).save()
        return {'name': phone.name}, 200


class SmartphonesApi(Resource):

    def put(self, name):
        body = request.get_json()
        Smartphone.objects.get(name=name).update(**body)
        return '', 200

    def delete(self, name):
        phone = Smartphone.objects.get(name=name).delete()
        return '', 200

    def get(self, name):
        # id = uuid.UUID(id)
        # print(id)
        phones = Smartphone.objects.get(name=name).to_json()
        return Response(phones, mimetype='application/json', status=200)


class CustomerApi(Resource):

    def get(self):
        customers = Customer.objects.to_json()
        return Response(customers, mimetype='application/json', status=200)

    def post(self):
        body = request.get_json()
        customer = Customer(**body).save()
        return {'name': customer.customer_name}, 200


class CustomersApi(Resource):

    def get(self, id):
        customers = Customer.objects.get(_id=id).to_json()
        return Response(customers, mimetype='application/json', status=200)

    def put(self, id):
        body = request.get_json()
        Customer.objects.get(_id=id).update(**body)
        return '', 200

    def delete(self, id):
        user = Customer.objects.get(_id=id).delete()
        return '', 200


class OrdersApi(Resource):

    def get(self):
        orders = Orders.objects.to_json()
        return Response(orders, mimetype='application/json', status=200)

    def post(self):
        body = request.get_json()
        order = Orders(**body).save()
        mname1 = Smartphone.objects.get(name=order.mname).to_json()
        return {'Mobile Name': order.mname}, 200