from flask_restful import Api

from .resources import DriverResources, DriversResources

def register_routes(api: Api):
    api.add_resource(DriverResources, "/driver")
    api.add_resource(DriversResources, "/get-drivers")