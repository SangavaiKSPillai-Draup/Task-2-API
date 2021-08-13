from controllers.controller import SmartphoneApi, CustomerApi, SmartphonesApi, CustomersApi, OrdersApi


def initialize_routes(api):
    api.add_resource(SmartphoneApi, '/smartphones')
    api.add_resource(SmartphonesApi, '/smartphones/<name>')
    api.add_resource(CustomerApi, '/customers')
    api.add_resource(CustomersApi, '/customers/<id>')
    api.add_resource(OrdersApi, '/orders')