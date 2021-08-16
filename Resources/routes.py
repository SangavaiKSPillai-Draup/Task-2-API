from controllers.controller import SmartphoneApi, CustomerApi, SmartphonesApi, CustomersApi, OrdersApi
from Resources.auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(SmartphoneApi, '/smartphones')
    api.add_resource(SmartphonesApi, '/smartphones/<name>')
    api.add_resource(CustomerApi, '/customers')
    api.add_resource(CustomersApi, '/customers/<id>')
    api.add_resource(OrdersApi, '/orders')
    api.add_resource(SignupApi, '/auth/signup')
    api.add_resource(LoginApi, '/auth/login')