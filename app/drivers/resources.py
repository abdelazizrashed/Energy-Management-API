from ast import Delete
from lib2to3.pgen2.driver import Driver
from flask_restful import Resource, reqparse, request

from ..shared.helpers.api_helpers import getFailedResponse, getSuccessResponse
from .services import DriverServices
from .models import DriverModel


_driver_parser = reqparse.RequestParser()
_driver_parser.add_argument("date", type=str)
_driver_parser.add_argument("unit_id", type=int)
_driver_parser.add_argument("energy", type=float)
_driver_parser.add_argument("expected_demand", type=float)
_driver_parser.add_argument("intensity_index", type=float)
_driver_parser.add_argument("difference", type=float)
_driver_parser.add_argument("cusum", type=float)



class DriverResources(Resource):
    def get(self):
        args = _driver_parser.parse_args()
        date = args["date"]
        if not date:
            return getFailedResponse([], "date is required"), 400
        driver = DriverServices.retrieve(date)
        if not driver:
            return getFailedResponse([], "Driver not found"), 404
        return getSuccessResponse(driver.to_json(), "Success"), 200

    def post(self):
        args = _driver_parser.parse_args()
        energy = args["energy"]
        unit_id = args["unit_id"]
        date = args["date"]
        if DriverServices.retrieve(date):
            return getFailedResponse([], "an element with date already exists"), 409

        if not energy:
            return getFailedResponse([], "energy is required"), 400
        if not unit_id:
            return getFailedResponse([], "unit_id is required"), 400
        driver = DriverModel.from_json(args)
        driver = DriverServices.create(driver)
        return getSuccessResponse(driver.to_json(), "Success"), 200

    def put(self):
        args = _driver_parser.parse_args()
        date = args["date"]
        if not date:
            return getFailedResponse([], "date is required"), 400
        driver = DriverModel.from_json(args)
        driver = DriverServices.update(driver)
        return getSuccessResponse(driver.to_json(), "Success"), 200

    def delete(self):
        args = _driver_parser.parse_args()
        date = args["date"]

        if not date:
            return getFailedResponse([], "date is required"), 400
        if not DriverServices.retrieve(date):
            return getFailedResponse([], "date wasn't found"), 404

        DriverServices.delete(DriverModel.from_json(args))
        return getSuccessResponse(date, "Success"), 200


class DriversResources(Resource):
    def get(self):
        drivers = DriverServices.retrieve_all()
        data = []
        for driver in drivers:
            data.append(driver.to_json())

        return getSuccessResponse(data, "Success"), 200
