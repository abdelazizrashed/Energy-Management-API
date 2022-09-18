from ..shared.db import db

from .models import MonthlyEnergyConsumtionModel

class MonthlyEnergyConsumtionServices:
    @staticmethod
    def create(driver: MonthlyEnergyConsumtionModel) ->MonthlyEnergyConsumtionModel:
        db.session.add(driver)
        db.session.commit()
        return driver
        

    @staticmethod
    def retrieve(month: str,source_id: int) ->MonthlyEnergyConsumtionModel:
        return MonthlyEnergyConsumtionModel.query.filter_by(month=month, source_id=source_id).first()

    @staticmethod
    def retrieve_all() -> list[MonthlyEnergyConsumtionModel]:
        return MonthlyEnergyConsumtionModel.query.all()

    @staticmethod
    def update(driver: MonthlyEnergyConsumtionModel) ->MonthlyEnergyConsumtionModel:
        if not MonthlyEnergyConsumtionServices.retrieve(driver.date):
            return MonthlyEnergyConsumtionServices.create(driver)
        
        db.session.commit()
        return driver

    @staticmethod
    def delete(driver: MonthlyEnergyConsumtionModel) -> None:
        temp_driver = MonthlyEnergyConsumtionServices.retrieve(driver.month)
        if temp_driver:
            db.session.delete(temp_driver)
            db.session.commit()
