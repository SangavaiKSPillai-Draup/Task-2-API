from flask_mongoengine import MongoEngine
# from flask_security import Security
from flask_mail import Mail, Message

db = MongoEngine()
# security = Security()
mail = Mail()


def initialize_db(app):
    db.init_app(app)
    return db


def initialize_mail(app):
    mail.init_app(app)

# def initialize_security(app, user_datastore):
#    security.init_app(app, user_datastore)
