from .models import EnergySourceModel


from ..shared.db import db


class EnergySourceServices:
    @staticmethod
    def create(source: EnergySourceModel) -> EnergySourceModel:
        db.session.add(source)
        db.session.commit()
        return source

    @staticmethod
    def update( source: EnergySourceModel) -> EnergySourceModel:
        if not EnergySourceServices.retrieve(source.source_id):
            return EnergySourceServices.create(source)
        
        db.session.commit()
        return source
        

    @staticmethod 
    def retrieve(source_id: int) -> EnergySourceModel:
        return EnergySourceModel.query.filter_by(source_id=source_id).first()


    @staticmethod 
    def retrieve_all()-> list[EnergySourceModel]:
        return EnergySourceModel.query.all()

    @staticmethod
    def delete(source: EnergySourceModel) :
        temp =   EnergySourceServices.retrieve(source.source_id)
        if temp:
            db.session.delete(temp)
            db.session.commit()
            
