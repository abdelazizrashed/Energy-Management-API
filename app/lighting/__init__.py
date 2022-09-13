from flask_restful import Api

from .resources import LightingResource, LightingsResource

def register_routes(api: Api):
    api.add_resource(LightingResource, "/lighting")
    api.add_resource(LightingsResource, "/get-all-lighting-data")