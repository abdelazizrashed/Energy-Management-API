from ast import Delete
from flask_restful import Resource, reqparse, request

from ..shared.helpers.api_helpers import getFailedResponse, getSuccessResponse
from .services import EnergySEUServices
from .models import EnergySEUModel


_source_parser = reqparse.RequestParser()
_source_parser.add_argument("type", type=str)
_source_parser.add_argument("main_driver", type=str)
_source_parser.add_argument("meter_type", type=str)
_source_parser.add_argument("source_id", type=int)
_source_parser.add_argument("objective", type=str)
_source_parser.add_argument("influencer", type=str)
_source_parser.add_argument("target", type=float)


class EnergySEUResource(Resource):
    def get(self):
        source_args = request.args
        source_id = source_args.get("type")
        if not source_id:
            return getFailedResponse([], "type is required"), 400
        source = EnergySEUServices.retrieve(source_id)
        if not source:
            return getFailedResponse([], "Energy source not found"), 404
        return getSuccessResponse(source.to_json(), "Success"), 200

    def post(self):
        args = _source_parser.parse_args()
        type = args.get("type")
        main_driver = args.get("main_driver")
        meter_type = args.get("meter_type")
        source_id = args.get("source_id")
        objective = args.get("objective")
        influencer = args.get("influencer")
        target = args.get("target")
        if not type:
            return getFailedResponse([], "type is required"), 400
        if not main_driver:
            return getFailedResponse([], "main_driver is required"), 400
        if not meter_type:
            return getFailedResponse([], "meter_type is required"), 400
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        if not objective:
            return getFailedResponse([], "objective is required"), 400
        if not influencer:
            return getFailedResponse([], "influencer is required"), 400
        if not target:
            return getFailedResponse([], "target is required"), 400
        
        source = EnergySEUServices.retrieve(type)
        if source:
            return getFailedResponse([], "SEU already exists"), 400

        
        source = EnergySEUModel.from_json(args)
        source = EnergySEUServices.create(source)
        return getSuccessResponse(source.to_json(), "Success"), 200

    def put(self):

        args = _source_parser.parse_args()
        type = args["type"]
        main_driver = args["main_driver"]
        meter_type = args["meter_type"]
        source_id = args["source_id"]
        objective = args["objective"]
        influencer = args["influencer"]
        target = args["target"]
        if not type:
            return getFailedResponse([], "type is required"), 400
        if not main_driver:
            return getFailedResponse([], "main_driver is required"), 400
        if not meter_type:
            return getFailedResponse([], "meter_type is required"), 400
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        if not objective:
            return getFailedResponse([], "objective is required"), 400
        if not influencer:
            return getFailedResponse([], "influencer is required"), 400
        if not target:
            return getFailedResponse([], "target is required"), 400
        source = EnergySEUModel.from_json(args)
        source = EnergySEUServices.update(source)
        return getSuccessResponse(source.to_json(), "Success"), 200

    def delete(self):

        args = _source_parser.parse_args()
        type = args["type"]
        if not type:
            return getFailedResponse([], "type is required"), 400
        EnergySEUServices.delete(EnergySEUModel.from_json(args))
        return getSuccessResponse(type, "Success"), 200


class EnergySEUsResource(Resource):
    def get(self):
        sources = EnergySEUServices.retrieve_all()
        data = []
        for source in sources:
            data.append(source.to_json())
        print(data)

        return getSuccessResponse(data, "Success"), 200
