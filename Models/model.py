from configuration.config import db
import datetime


class Smartphone(db.Document):
    name = db.StringField(required=True, unique=True)
    manufacturer = db.StringField(required=True)
    cost = db.FloatField(required=True)


"""
class SmartphoneFeatures(db.Document):
    series = db.StringField(required=True)
    camera_mp = db.IntField(required=True)
    battery_ah = db.IntField(required=True)
    operating_system = db.StringField(required=True)


class Customer(db.Document):
    _id = db.IntField(required=True, unique=True)
    customer_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    age = db.IntField(required=True)


class Orders:
    _id = db.IntField(required=True, unique=True)
    mid = db.UUIDField(required=True, unique=True)
    order_date = db.DateTimeField(default=datetime.datetime.date)
    Email_sent = db.BooleanField(default='NO')
"""

