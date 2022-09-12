from flask_restful import Api

from .resources import MonthlyEnergyConsumtionResource, MonthlyEnergyConsumtionsResource

def register_routes(api: Api):
    api.add_resource(MonthlyEnergyConsumtionResource, "/monthly-energy-consumtion")
    api.add_resource(MonthlyEnergyConsumtionsResource, "/get-all-monthly-energy-consumtion")