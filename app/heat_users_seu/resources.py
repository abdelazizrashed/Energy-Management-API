from flask_restful import Resource, reqparse, request

from ..shared.helpers.api_helpers import getFailedResponse, getSuccessResponse
from .services import HeatUserServices
from .models import HeatUserModel
from ..energy_seu.services import EnergySEUServices


_unit_parser = reqparse.RequestParser()
_unit_parser.add_argument("id", type=int)
_unit_parser.add_argument("process_type", type=str)
_unit_parser.add_argument("name_plate", type=str)
_unit_parser.add_argument("vsd_speed", type=float)
_unit_parser.add_argument("load", type=float)
_unit_parser.add_argument("actual_power", type=float)
_unit_parser.add_argument("annual_power", type=float)
_unit_parser.add_argument("note", type=str)
_unit_parser.add_argument("off_times", type=str)
_unit_parser.add_argument("percent_total", type=float)
_unit_parser.add_argument("estimation_process", type=str)
_unit_parser.add_argument("improvments", type=str)
_unit_parser.add_argument("purpose", type=str)
_unit_parser.add_argument("type", type=str)
_unit_parser.add_argument("is_yearly", type=bool)


class HeatUserResource(Resource):
    def get(self):
        unit_args = request.args
        id = unit_args.get("id")
        if not id:
            return getFailedResponse([], "id is required"), 400
        unit = HeatUserServices.retrieve(id)
        if not unit:
            return getFailedResponse([], "Energy Unit not found"), 404
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def post(self):
        args = _unit_parser.parse_args()
        type = args.get("process_type")
        if not type: 
            return getFailedResponse([], "process_type is required"), 400
        seu = EnergySEUServices.retrieve(type)
        if not seu:
            return getFailedResponse([], "process_type doesn't exist"), 400

        if len(args.items()) == 0:
            return getFailedResponse([], "add some data"), 400
        unit = HeatUserModel.from_json(args)
        unit = HeatUserServices.create(unit)
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def put(self):
        args = _unit_parser.parse_args()
        id = args["id"]
        if not id:
            return getFailedResponse([], "id is required"), 400
        type = args.get("process_type")
        if not type: 
            return getFailedResponse([], "process_type is required"), 400
        seu = EnergySEUServices.retrieve(type)
        if not seu:
            return getFailedResponse([], "process_type doesn't exist"), 400
            
        if len(args.items()) == 1:
            return getFailedResponse([], "add some data"), 400
        unit = HeatUserModel.from_json(args)
        unit = HeatUserServices.update(unit)
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def delete(self):
        unit_args = request.args
        id = unit_args.get("id")
        if not id:
            return getFailedResponse([], "id is required"), 400
            
        HeatUserServices.delete(id)
        return getSuccessResponse(id, "Success"), 200


class HeatUsersResource(Resource):
    def get(self):
        units = HeatUserServices.retrieve_all()
        data = []
        for unit in units:
            data.append(unit.to_json())

        return getSuccessResponse(data, "Success"), 200
