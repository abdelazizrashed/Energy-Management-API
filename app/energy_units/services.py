from .models import EnergyUnitModel


from ..shared.db import db


class EnergyUnitServices:
    @staticmethod
    def create(unit: EnergyUnitModel) -> EnergyUnitModel:
        db.session.add(unit)
        db.session.commit()
        return unit

    @staticmethod
    def update( unit: EnergyUnitModel) -> EnergyUnitModel:
        if not EnergyUnitServices.retrieve(unit.unit_id):
            return EnergyUnitServices.create(unit)
        
        db.session.commit()
        return unit

    @staticmethod 
    def retrieve(unit_id: int) -> EnergyUnitModel:
        return EnergyUnitModel.query.filter_by(unit_id=unit_id).first()


    @staticmethod 
    def retrieve_all()-> list[EnergyUnitModel]:
        return EnergyUnitModel.query.all();

    @staticmethod
    def delete(unit: EnergyUnitModel) :
        temp_unit =  EnergyUnitServices.retrieve(unit.unit_id)
        if temp_unit:
            db.session.delete(temp_unit)
            db.session.commit()
            
