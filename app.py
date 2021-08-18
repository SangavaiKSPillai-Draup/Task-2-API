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
initialize_routes(api)
initialize_mail(app)
app.run(debug=True)