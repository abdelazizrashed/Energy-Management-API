from ast import Delete
from flask_restful import Resource, reqparse, request

from ..shared.helpers.api_helpers import getFailedResponse, getSuccessResponse
from .services import AnnualTrendsServices
from .models import AnnualTrendsModel


_source_parser = reqparse.RequestParser()
_source_parser.add_argument("source_id", type=int)
_source_parser.add_argument("unit_id", type=int)
_source_parser.add_argument("consumption", type=float)
_source_parser.add_argument("cost", type=float)
_source_parser.add_argument("unit_price", type=float)
_source_parser.add_argument("budget", type=float)
_source_parser.add_argument("target", type=float)
_source_parser.add_argument("type", type=str)
_source_parser.add_argument("date", type=str)


class AnnualTrendResource(Resource):
    def get(self):
        source_args = _source_parser.parse_args()
        date = source_args["date"]
        if not date:
            return getFailedResponse([], "date is required"), 400
        source = AnnualTrendsServices.retrieve(date)
        if not source:
            return getFailedResponse([], "Annual trend not found"), 404
        return getSuccessResponse(source.to_json(), "Success"), 200

    def post(self):
        args = _source_parser.parse_args()
        source_id = args["source_id"]
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        unit_id = args["unit_id"]
        if not unit_id:
            return getFailedResponse([], "unit_id is required"), 400
        consumption = args["consumption"]
        if not consumption:
            return getFailedResponse([], "consumption is required"), 400
        cost = args["cost"]
        if not cost:
            return getFailedResponse([], "cost is required"), 400
        unit_price = args["unit_price"]
        if not unit_price:
            return getFailedResponse([], "unit_price is required"), 400
        budget = args["budget"]
        if not budget:
            return getFailedResponse([], "budget is required"), 400
        target = args["target"]
        if not target:
            return getFailedResponse([], "target is required"), 400
        type = args["type"]
        if not type:
            return getFailedResponse([], "type is required"), 400
        date = args["date"]
        if not date:
            return getFailedResponse([], "date is required"), 400
        source = AnnualTrendsModel.from_json(args)
        source = AnnualTrendsServices.create(source)
        return getSuccessResponse(source.to_json(), "Success"), 200

    def put(self):

        args = _source_parser.parse_args()
        source_id = args["source_id"]
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        unit_id = args["unit_id"]
        if not unit_id:
            return getFailedResponse([], "unit_id is required"), 400
        consumption = args["consumption"]
        if not consumption:
            return getFailedResponse([], "consumption is required"), 400
        cost = args["cost"]
        if not cost:
            return getFailedResponse([], "cost is required"), 400
        unit_price = args["unit_price"]
        if not unit_price:
            return getFailedResponse([], "unit_price is required"), 400
        budget = args["budget"]
        if not budget:
            return getFailedResponse([], "budget is required"), 400
        target = args["target"]
        if not target:
            return getFailedResponse([], "target is required"), 400
        type = args["type"]
        if not type:
            return getFailedResponse([], "type is required"), 400
        date = args["date"]
        if not date:
            return getFailedResponse([], "date is required"), 400
        source = AnnualTrendsModel.from_json(args)
        source = AnnualTrendsServices.update(source)
        return getSuccessResponse(source.to_json(), "Success"), 200

    def delete(self):

        args = _source_parser.parse_args()
        date = args["date"]
        if not date:
            return getFailedResponse([], "date is required"), 400
        source = AnnualTrendsModel.from_json(args)
        AnnualTrendsServices.delete(source)
        return getSuccessResponse(date, "Success"), 200


class AnnualTrendsResource(Resource):
    def get(self):
        sources = AnnualTrendsServices.retrieve_all()
        data = []
        for source in sources:
            data.append(source.to_json())
        print(data)

        return getSuccessResponse(data, "Success"), 200
