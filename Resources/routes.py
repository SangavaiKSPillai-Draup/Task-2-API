from controllers.controller import SmartphoneApi


def initialize_routes(api):
    api.add_resource(SmartphoneApi, '/smartphones')
