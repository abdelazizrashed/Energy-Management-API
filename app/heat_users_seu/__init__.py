from flask_restful import Api

from .resources import HeatUserResource, HeatUsersResource

def register_routes(api: Api):
    api.add_resource(HeatUserResource, "/heat-user")
    api.add_resource(HeatUsersResource, "/get-all-heat-users")