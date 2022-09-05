from flask_restful import Api

from .resources import EnergySourceResource, EnergySourcesResource

def register_routes(api: Api):
    api.add_resource(EnergySourceResource, "/energy-source")
    api.add_resource(EnergySourcesResource, "/get-energy-sources")