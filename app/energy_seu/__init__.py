from flask_restful import Api

from .resources import EnergySEUResource, EnergySEUsResource

def register_routes(api: Api):
    api.add_resource(EnergySEUResource, "/energy-seu")
    api.add_resource(EnergySEUsResource, "/get-all-energy-seu")