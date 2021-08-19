"""
    This code deals with the configuration of the app.
    The database and mail objects are initialized here
"""

from flask_mongoengine import MongoEngine
from flask_mail import Mail

db = MongoEngine()
mail = Mail()


def initialize_db(app):
    """
        Initializes the MongoEngine database object
    """
    db.init_app(app)


def initialize_mail(app):
    """
        Initializes the Flask Mail object
    """
    mail.init_app(app)
