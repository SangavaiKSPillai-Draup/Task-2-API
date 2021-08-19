"""
This is the file from which Program execution begins.
"""
from flask import Flask
from configuration.config import initialize_db, initialize_mail
from flask_bcrypt import Bcrypt
from flask_restful import Api
from Resources.routes import initialize_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.config.from_envvar('ENV_FILE_LOCATION')
initialize_db(app)
initialize_routes(api)
initialize_mail(app)

if __name__ == "__main__":
    app.run(debug=True)
