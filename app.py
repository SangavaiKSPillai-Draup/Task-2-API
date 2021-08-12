from flask import Flask, jsonify
from configuration.config import initialize_db
from flask_restful import Api
from Resources.routes import initialize_routes
from Models.model import Smartphone

app = Flask(__name__)
api = Api(app)

# MONGO_URL = "mongodb://sangavai:admin@127.0.0.1:27017/"
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://sangavai:admin@127.0.0.1:27017/Mobile_Store?authSource=admin'
}
initialize_db(app)
initialize_routes(api)

app.run(debug=True)
