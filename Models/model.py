from dataclasses import dataclass
import uuid
from datetime import date

@dataclass
class Smartphone:
    mid: uuid
    name: str
    manufacturer: str
    cost: float
    series: str
    camera_mp: int
    battery_ah: int
    operating_system: str

@dataclass
class Customer:
    cid: str
    customer_name: str
    email: str
    age: int

@dataclass
class Orders:
    cid: str
    mid: str
    order_date: date
    Email_sent: bool





