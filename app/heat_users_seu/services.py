from ..shared.db import db

from .models import HeatUserModel


class HeatUserServices:
    @staticmethod
    def create(unit: HeatUserModel) -> HeatUserModel:
        db.session.add(unit)
        db.session.commit()
        return unit

    @staticmethod
    def update(unit: HeatUserModel) -> HeatUserModel:
        if not HeatUserServices.retrieve(unit.id):
            return HeatUserServices.create(unit)

        db.session.commit()
        return unit

    @staticmethod
    def retrieve(id: int) -> HeatUserModel:
        return HeatUserModel.query.filter_by(id=id).first()

    @staticmethod
    def retrieve_all() -> list[HeatUserModel]:
        return HeatUserModel.query.all()

    @staticmethod
    def delete(id: int):
        temp_unit = HeatUserServices.retrieve(id)
        if temp_unit:
            db.session.delete(temp_unit)
            db.session.commit()
