from ..shared.db import db

from .models import EnergySEUModel

class EnergySEUServices:
    @staticmethod
    def create(driver: EnergySEUModel) ->EnergySEUModel:
        db.session.add(driver)
        db.session.commit()
        return driver
        

    @staticmethod
    def retrieve(month: str) ->EnergySEUModel:
        return EnergySEUModel.query.filter_by(type=month).first()

    @staticmethod
    def retrieve_all() -> list[EnergySEUModel]:
        return EnergySEUModel.query.all()

    @staticmethod
    def update(driver: EnergySEUModel) ->EnergySEUModel:
        if not EnergySEUServices.retrieve(driver.type):
            return EnergySEUServices.create(driver)
        
        db.session.commit()
        return driver

    @staticmethod
    def delete(driver: EnergySEUModel) -> None:
        temp_driver = EnergySEUServices.retrieve(driver.type)
        if temp_driver:
            db.session.delete(temp_driver)
            db.session.commit()
