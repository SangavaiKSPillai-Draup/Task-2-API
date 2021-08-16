import datetime
import json
import uuid
import ast
from Models.model import Smartphone, Customer, Orders
from flask import Response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from Models.CustomErrors import *


class SmartphoneApi(Resource):
    def get(self):
        phones = Smartphone.objects.to_json()
        return Response(phones, mimetype='application/json', status=200)

    @jwt_required()
    def post(self):
        print(request)
        body = request.get_json()
        # print(body)
        phone = Smartphone(**body).save()
        return {'name': phone.name}, 200


class SmartphonesApi(Resource):

    @jwt_required()
    def put(self, name):
        try:
            body = request.get_json()
            Smartphone.objects.get(name=name).update(**body)
            return '', 200
        except Smartphone.DoesNotExist:
            str1 = "The phone does not exist"
            return str1, 404

    @jwt_required()
    def delete(self, name):
        try:
            phone = Smartphone.objects.get(name=name).delete()
            return '', 200
        except Smartphone.DoesNotExist:
            str1 = "The phone does not exist"
            return str1, 404

    def get(self, name):
        # id = uuid.UUID(id)
        # print(id)
        try:
            phones = Smartphone.objects.get(name=name).to_json()
            if phones == "":
                raise MobileNotFoundError("The phone doesn't exist")
            return Response(phones, mimetype='application/json', status=200)
        except MobileNotFoundError:
            str1 = name + " does not exist"
            return Response(str1, mimetype='application/json', status=404)


class CustomerApi(Resource):

    def get(self):
        customers = Customer.objects.to_json()
        return Response(customers, mimetype='application/json', status=200)

    @jwt_required()
    def post(self):
        body = request.get_json()
        customer = Customer(**body).save()
        return {'name': customer.customer_name}, 200


class CustomersApi(Resource):

    def get(self, id):
        try:
            customers = Customer.objects.get(_id=id).to_json()
            print(customers)
            if customers == "":
                raise CustomerNotFoundError("Customer does not exist")
            return Response(customers, mimetype='application/json', status=200)

        except Customer.DoesNotExist or CustomerNotFoundError:
            str1 = "The customer does not exist in our records"
            return Response(str1, mimetype='application/json', status=404)

    @jwt_required()
    def put(self, id):
        body = request.get_json()
        Customer.objects.get(_id=id).update(**body)
        return '', 200

    @jwt_required()
    def delete(self, id):
        user = Customer.objects.get(_id=id).delete()
        return '', 200


class OrdersApi(Resource):
    def get(self):
        orders = Orders.objects.to_json()
        # print(type(orders))
        demand = json.loads(orders)
        time_in_millis = demand[0]['order_date']['$date']
        dt = datetime.datetime.fromtimestamp(time_in_millis / 1000.0, tz=datetime.timezone.utc)
        demand[0]['order_date']['$date'] = dt.strftime("%Y-%m-%d")
        print(demand[0]['order_date']['$date'])
        orders = json.dumps(demand)
        return Response(orders, mimetype='application/json', status=200)

    @jwt_required()
    def post(self):
        c_update = SmartphonesApi()
        body = request.get_json()
        byte_str = c_update.get(body['mname']).get_data()
        dict_str = byte_str.decode("UTF-8")
        my_data = ast.literal_eval(dict_str)
        # print(my_data)
        try:
            if my_data['Stock'] == 0:
                raise MobileNotFoundError("Mobile Phone not present")
            my_data['Stock'] -= 1
            order = Orders(**body).save()
            Smartphone.objects(name=order.mname).update(dec__Stock=1)
            mname1 = Smartphone.objects.get(name=order.mname).to_json()
            mname2 = json.loads(mname1)
            # print(mname2)
            return {'Mobile Name': mname2['name']}, 200

        except MobileNotFoundError:
            str1 = my_data['name'] + " is out of stock"
            # print(my_data['name'], "is out of stock")
            return str1, 200
