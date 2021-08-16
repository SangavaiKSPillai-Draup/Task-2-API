import sys, random
from configuration.config import db
import datetime
from uuid import uuid4
from flask_bcrypt import generate_password_hash, check_password_hash

MAX = 50000


class Smartphone(db.Document):
    _id = db.UUIDField(default=uuid4(), primary_key=True)
    name = db.StringField(required=True, unique=True)
    manufacturer = db.StringField(required=True)
    cost = db.FloatField(required=True)
    Stock = db.IntField(required=True)
    camera_mp = db.IntField(required=True)
    battery_ah = db.IntField(required=True)
    operating_system = db.StringField()


class Customer(db.Document):
    _id = db.StringField(default="C0" + str(random.randint(0, MAX)), primary_key=True)
    customer_name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    age = db.IntField(default=18)
    # role = db.StringField(default='User')

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Orders(db.Document):
    mname = db.StringField(required=True)
    cid = db.StringField(required=True)
    order_date = db.DateTimeField(default=datetime.datetime.utcnow().strftime("%Y-%m-%d"))
    Email_sent = db.StringField(default='NO')
