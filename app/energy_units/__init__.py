from flask_restful import Api

from .resources import EnergyUnitResources, EnergyUnitsResources

def register_routes(api: Api):
    api.add_resource(EnergyUnitResources, "/energy-unit")
    api.add_resource(EnergyUnitsResources, "/get-energy-units")