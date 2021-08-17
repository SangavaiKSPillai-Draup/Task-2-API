from flask import Flask, jsonify
from configuration.config import initialize_db, initialize_mail
from flask_bcrypt import Bcrypt
from flask_restful import Api
from Resources.routes import initialize_routes
from Models.model import Smartphone, Customer
from flask_jwt_extended import JWTManager
# from flask_security import Security, MongoEngineUserDatastore
from flask_login import current_user
from flask_mail import Mail, Message
from os import environ as env

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
env['ENV_FILE_LOCATION'] = './.env'
env['FLASK_ENV'] = 'development'

# MONGO_URL = "mongodb://sangavai:admin@127.0.0.1:27017/"
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://sangavai:admin@127.0.0.1:27017/Mobile_Store?authSource=admin'
}
app.config.from_envvar('ENV_FILE_LOCATION')
db = initialize_db(app)
# user_datastore = MongoEngineUserDatastore(db, Customer, Role)
# security = Security(app, user_datastore)
initialize_routes(api)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '****'
app.config['MAIL_PASSWORD'] = '****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
initialize_mail(app)
app.run(debug=True)