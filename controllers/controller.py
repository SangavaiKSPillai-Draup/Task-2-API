"""
    This file contains the code that interacts with the database.
    It handles CRUD operations.

    There are two decorators used here.
    @jwt_required() - This decorator is used to check if a Token (Bearer token) is present in the Authorisation Header
    of an HTTP request
    @roles_required() - This checks for the role of a particular user logged in to the application.
"""
import datetime
import json
import ast
from Models.model import Smartphone, Customer, Orders
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from Models.CustomErrors import *
from configuration.config import mail
from flask_mail import Message
from controllers.role_decorator import roles_required


class SmartphoneApi(Resource):
    """
    Retrieving details of all mobiles, and adding a new mobile to the database\n
    GET - to retrieve all smartphones in the database\n
    POST - to add a new smartphone to the database\n
    """
    def get(self):
        phones = Smartphone.objects.to_json()
        return Response(phones, mimetype='application/json', status=200)

    @jwt_required()
    @roles_required(['admin'])
    def post(self):
        print(request)
        body = request.get_json()
        # print(body)
        phone = Smartphone(**body).save()
        return {'name': phone.name}, 200


class SmartphonesApi(Resource):
    """
        Retrieving/Updating details of a particular mobile. \n
        GET - Retrieve a particular smartphone's details by passing name as parameter\n
        PUT/UPDATE - Update the details of a particular phone by passing name as argument\n
        DELETE - Remove a particular phone from the database, by passing the phone's name as argument\n
    """
    @jwt_required()
    @roles_required(['admin'])
    def put(self, name):
        try:
            body = request.get_json()
            Smartphone.objects.get(name=name).update(**body)
            return '', 200
        except Smartphone.DoesNotExist:
            str1 = "The phone does not exist"
            return str1, 404

    @jwt_required()
    @roles_required(['admin'])
    def delete(self, name):
        try:
            phone = Smartphone.objects.get(name=name).delete()
            return '', 200
        except Smartphone.DoesNotExist:
            str1 = "The phone does not exist"
            return str1, 404

    def get(self, name):
        try:
            phones = Smartphone.objects.get(name=name).to_json()
            if phones == "":
                raise MobileNotFoundError("The phone doesn't exist")
            return Response(phones, mimetype='application/json', status=200)
        except MobileNotFoundError:
            str1 = name + " does not exist"
            return Response(str1, mimetype='application/json', status=404)


class CustomerApi(Resource):
    """
        Retrieving details of all customers, and adding a new customer to the database.
        GET - Get all details of customers registered.
        POST - Add details of a new customer
    """
    @jwt_required()
    @roles_required(['admin'])
    def get(self):
        customers = Customer.objects.to_json()
        return Response(customers, mimetype='application/json', status=200)

    @jwt_required()
    @roles_required(['admin'])
    def post(self):
        body = request.get_json()
        customer = Customer(**body).save()
        return {'name': customer.customer_name}, 200


class CustomersApi(Resource):
    """
        Retrieving details of a particular customer, as well as updating a customer's details, and/or deleting a customer.
        GET - Retrieve details of a particular customer, by passing Customer ID as argument
        PUT - Update details of a particular customer, by passing Customer ID as argument
        DELETE - Remove a customer from the database, by passing Customer ID as argument
    """

    @jwt_required()
    @roles_required(['admin'])
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
    @roles_required(['admin'])
    def put(self, id):
        body = request.get_json()
        Customer.objects.get(_id=id).update(**body)
        return '', 200

    @jwt_required()
    @roles_required(['admin'])
    def delete(self, id):
        user = Customer.objects.get(_id=id).delete()
        return '', 200


class OrdersApi(Resource):
    """
        Retrieve order details, as well as placing a new order by customer.
        GET - get all orders taken in the database
        POST - customer orders a new mobile
    """
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
    @roles_required(['user'])
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
            str2 = "You have ordered: " + my_data['name']
            user_id = get_jwt_identity()
            user = Customer.objects.get(_id=user_id).to_json()
            user1 = json.loads(user)
            email = user1['email']
            msg = Message('order details', sender='umadevipaiaz345@gmail.com', recipients=[email])
            # print(mname2)
            msg.body = str2
            mail.send(msg)
            return {'Mobile Name': mname2['name']}, 200

        except MobileNotFoundError:
            str1 = my_data['name'] + " is out of stock"
            # print(my_data['name'], "is out of stock")
            return str1, 200
