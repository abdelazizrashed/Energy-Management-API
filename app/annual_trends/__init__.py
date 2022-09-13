from flask_restful import Api

from .resources import AnnualTrendResource, AnnualTrendsResource

def register_routes(api: Api):
    api.add_resource(AnnualTrendResource, "/annual-trend")
    api.add_resource(AnnualTrendsResource, "/get-all-annual-trends")