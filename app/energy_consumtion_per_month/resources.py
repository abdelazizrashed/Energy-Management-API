from flask_restful import Resource, reqparse, request

from ..shared.helpers.api_helpers import getFailedResponse, getSuccessResponse
from .services import MonthlyEnergyConsumtionServices
from .models import MonthlyEnergyConsumtionModel


_unit_parser = reqparse.RequestParser()
_unit_parser.add_argument("cost", type=int)
_unit_parser.add_argument("month", type=str)
_unit_parser.add_argument("usage", type=int)
_unit_parser.add_argument("unit_id", type=int)
_unit_parser.add_argument("source_id", type=int)

    # month = db.Column(db.String(), primary_key=True)
    # cost = db.Column(db.Integer, nullable=False)
    # usage = db.Column(db.Integer, nullable=False)
    # unit_id = db.Column(db.Integer, db.ForeignKey(
    #     f'{EnergyUnitModel.__tablename__}.unit_id'), nullable=False)
    # source_id = db.Column(db.Integer, db.ForeignKey(
        # f'{EnergyUnitModel.__tablename__}.source_id'), nullable=False)


class MonthlyEnergyConsumtionResource(Resource):
    def get(self):
        unit_args = request.args
        
        if not unit_args:
            return getFailedResponse([], "month and source_id are required"), 400
        month = unit_args.get("month")
        if not month:
            return getFailedResponse([], "month is required"), 400
        source_id = unit_args.get("source_id")
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        unit = MonthlyEnergyConsumtionServices.retrieve(month, source_id)
        if not unit:
            return getFailedResponse([], "Energy Unit not found"), 404
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def post(self):
        args = _unit_parser.parse_args()
        cost = args["cost"]
        if not cost:
            return getFailedResponse([], "cost is required"), 400
        month = args["month"]
        if not month:
            return getFailedResponse([], "month is required"), 400
        usage = args["usage"]
        if not usage:
            return getFailedResponse([], "usage is required"), 400
        unit_id = args["unit_id"]
        if not unit_id:
            return getFailedResponse([], "unit_id is required"), 400
        source_id = args["source_id"]
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        unit = MonthlyEnergyConsumtionModel.from_json(args)
        unit = MonthlyEnergyConsumtionServices.create(unit)
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def put(self):

        args = _unit_parser.parse_args()
        cost = args["cost"]
        if not cost:
            return getFailedResponse([], "cost is required"), 400
        month = args["month"]
        if not month:
            return getFailedResponse([], "month is required"), 400
        usage = args["usage"]
        if not usage:
            return getFailedResponse([], "usage is required"), 400
        unit_id = args["unit_id"]
        if not unit_id:
            return getFailedResponse([], "unit_id is required"), 400
        source_id = args["source_id"]
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        unit = MonthlyEnergyConsumtionModel.from_json(args)
        unit = MonthlyEnergyConsumtionServices.update(unit)
        return getSuccessResponse(unit.to_json(), "Success"), 200

    def delete(self):

        unit_args = request.args
        
        if not unit_args:
            return getFailedResponse([], "month and source_id are required"), 400
        month = unit_args.get("month")
        if not month:
            return getFailedResponse([], "month is required"), 400
        source_id = unit_args.get("source_id")
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        MonthlyEnergyConsumtionServices.delete(month, source_id)
        return getSuccessResponse(month, "Success"), 200


class MonthlyEnergyConsumtionsResource(Resource):
    def get(self):
        units = MonthlyEnergyConsumtionServices.retrieve_all()
        data = []
        for unit in units:
            data.append(unit.to_json())

        return getSuccessResponse(data, "Success"), 200
