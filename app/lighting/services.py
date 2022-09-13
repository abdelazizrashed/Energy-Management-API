from ..shared.db import db

from .models import LightingModel


class LightingServices:
    @staticmethod
    def create(unit: LightingModel) -> LightingModel:
        db.session.add(unit)
        db.session.commit()
        return unit

    @staticmethod
    def update(unit: LightingModel) -> LightingModel:
        if not LightingServices.retrieve(unit.id):
            return LightingServices.create(unit)

        db.session.commit()
        return unit

    @staticmethod
    def retrieve(id: int) -> LightingModel:
        return LightingModel.query.filter_by(id=id).first()

    @staticmethod
    def retrieve_all() -> list[LightingModel]:
        return LightingModel.query.all()

    @staticmethod
    def delete(id: int):
        temp_unit = LightingServices.retrieve(id)
        if temp_unit:
            db.session.delete(temp_unit)
            db.session.commit()
