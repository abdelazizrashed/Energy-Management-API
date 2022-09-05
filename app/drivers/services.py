from ..shared.db import db

from .models import DriverModel

class DriverServices:
    @staticmethod
    def create(driver: DriverModel) ->DriverModel:
        db.session.add(driver)
        db.session.commit()
        return driver
        

    @staticmethod
    def retrieve(date: str) ->DriverModel:
        return DriverModel.query.filter_by(date=date).first()

    @staticmethod
    def retrieve_all() -> list[DriverModel]:
        return DriverModel.query.all()

    @staticmethod
    def update(driver: DriverModel) ->DriverModel:
        if not DriverServices.retrieve(driver.date):
            return DriverServices.create(driver)
        
        db.session.commit()
        return driver

    @staticmethod
    def delete(driver: DriverModel) -> None:
        temp_driver = DriverServices.retrieve(driver.date)
        if temp_driver:
            db.session.delete(temp_driver)
            db.session.commit()
