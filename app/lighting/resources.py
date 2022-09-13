from flask_restful import Resource, reqparse, request

from ..shared.helpers.api_helpers import getFailedResponse, getSuccessResponse
from .services import LightingServices
from .models import LightingModel


_unit_parser = reqparse.RequestParser()
_unit_parser.add_argument("unit_id", type=int)
_unit_parser.add_argument("name", type=str)

_unit_parser.add_argument("id", type=int)
_unit_parser.add_argument("process_type", type=str)
_unit_parser.add_argument("area", type=str)
_unit_parser.add_argument("category", type=str)
_unit_parser.add_argument("fitting_type", type=str)
_unit_parser.add_argument("fitting_no", type=float)
_unit_parser.add_argument("lamp_rating", type=float)
_unit_parser.add_argument("lamp_no", type=float)
_unit_parser.add_argument("hours_per_year", type=float)
_unit_parser.add_argument("kwh_per_year", type=float)
_unit_parser.add_argument("light_control", type=str)
_unit_parser.add_argument("improvments", type=str)
_unit_parser.add_argument("lux_levels_available", type=str)
_unit_parser.add_argument("required_lux_level", type=float)
_unit_parser.add_argument("actual_lux_level", type=float)
_unit_parser.add_argument("natural_lighting", type=str)
_unit_parser.add_argument("month", type=str)


class LightingResource(Resource):
    def get(self):
        unit_args = _unit_parser.parse_args()
        id = unit_args["id"]
        if not id:
            return getFailedResponse([], "id is required"), 400
        unit = LightingServices.retrieve(id)
        if not unit:
            return getFailedResponse([], "Energy Unit not found"), 404
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def post(self):
        args = _unit_parser.parse_args()
        if len(args.items) == 0:
            return getFailedResponse([], "add some data"), 400
        unit = LightingModel.from_json(args)
        unit = LightingServices.create(unit)
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def put(self):

        args = _unit_parser.parse_args()
        id = args["id"]
        if not id:
            return getFailedResponse([], "id is required"), 400
            
        if len(args.items) == 1:
            return getFailedResponse([], "add some data"), 400
        unit = LightingModel.from_json(args)
        unit = LightingServices.update(unit)
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def delete(self):

        args = _unit_parser.parse_args()
        id = args["id"]
        if not id:
            return getFailedResponse([], "id is required"), 400
        LightingServices.delete(id)
        return getSuccessResponse(id, "Success"), 200


class LightingsResource(Resource):
    def get(self):
        units = LightingServices.retrieve_all()
        data = []
        for unit in units:
            data.append(unit.to_json())

        return getSuccessResponse(data, "Success"), 200
