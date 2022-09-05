from ast import Delete
from flask_restful import Resource, reqparse, request

from ..shared.helpers.api_helpers import getFailedResponse, getSuccessResponse
from .services import EnergySourceServices
from .models import EnergySourceModel


_source_parser = reqparse.RequestParser()
_source_parser.add_argument("source_id", type=int)
_source_parser.add_argument("name", type=str)


class EnergySourceResource(Resource):
    def get(self):
        source_args = _source_parser.parse_args()
        source_id = source_args["source_id"]
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        source = EnergySourceServices.retrieve(source_id)
        if not source:
            return getFailedResponse([], "Energy source not found"), 404
        return getSuccessResponse(source.to_json(), "Success"), 200

    def post(self):
        args = _source_parser.parse_args()
        name = args["name"]
        if not name:
            return getFailedResponse([], "name is required"), 400
        source = EnergySourceModel(None, name)
        source = EnergySourceServices.create(source)
        return getSuccessResponse(source.to_json(), "Success"), 200

    def put(self):

        args = _source_parser.parse_args()
        name = args["name"]
        source_id = args["source_id"]
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        if not name:
            return getFailedResponse([], "name is required"), 400
        source = EnergySourceModel(source_id, name)
        source = EnergySourceServices.update(source)
        return getSuccessResponse(source.to_json(), "Success"), 200

    def delete(self):

        args = _source_parser.parse_args()
        source_id = args["source_id"]
        if not source_id:
            return getFailedResponse([], "source_id is required"), 400
        EnergySourceServices.delete(EnergySourceModel(source_id, None))
        return getSuccessResponse(source_id, "Success"), 200


class EnergySourcesResource(Resource):
    def get(self):
        sources = EnergySourceServices.retrieve_all()
        data = []
        for source in sources:
            data.append(source.to_json())
        print(data)

        return getSuccessResponse(data, "Success"), 200
