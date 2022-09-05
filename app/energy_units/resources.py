from flask_restful import Resource, reqparse, request

from ..shared.helpers.api_helpers import getFailedResponse, getSuccessResponse
from .services import EnergyUnitServices
from .models import EnergyUnitModel


_unit_parser = reqparse.RequestParser()
_unit_parser.add_argument("unit_id", type=int)
_unit_parser.add_argument("name", type=str)


class EnergyUnitResources(Resource):
    def get(self):
        unit_args = _unit_parser.parse_args()
        unit_id = unit_args["unit_id"]
        if not unit_id:
            return getFailedResponse([], "unit_id is required"), 400
        unit = EnergyUnitServices.retrieve(unit_id)
        if not unit:
            return getFailedResponse([], "Energy Unit not found"), 404
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def post(self):
        args = _unit_parser.parse_args()
        name = args["name"]
        if not name:
            return getFailedResponse([], "name is required"), 400
        unit = EnergyUnitModel(None, name)
        unit = EnergyUnitServices.create(unit)
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def put(self):

        args = _unit_parser.parse_args()
        name = args["name"]
        unit_id = args["unit_id"]
        if not unit_id:
            return getFailedResponse([], "unit_id is required"), 400
        if not name:
            return getFailedResponse([], "name is required"), 400
        unit = EnergyUnitModel(unit_id, name)
        unit = EnergyUnitServices.update(unit)
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def delete(self):

        args = _unit_parser.parse_args()
        unit_id = args["unit_id"]
        if not unit_id:
            return getFailedResponse([], "unit_id is required"), 400
        EnergyUnitServices.delete(EnergyUnitModel(unit_id, None))
        return getSuccessResponse(unit_id, "Success"), 200


class EnergyUnitsResources(Resource):
    def get(self):
        units = EnergyUnitServices.retrieve_all()
        data = []
        for unit in units:
            data.append(unit.to_json())

        return getSuccessResponse(data, "Success"), 200
