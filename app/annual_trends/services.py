from .models import AnnualTrendsModel


from ..shared.db import db


class AnnualTrendsServices:
    @staticmethod
    def create(source: AnnualTrendsModel) -> AnnualTrendsModel:
        db.session.add(source)
        db.session.commit()
        return source

    @staticmethod
    def update( source: AnnualTrendsModel) -> AnnualTrendsModel:
        if not AnnualTrendsServices.retrieve(source.date):
            return AnnualTrendsServices.create(source)
        
        db.session.commit()
        return source
        

    @staticmethod 
    def retrieve(date: str) -> AnnualTrendsModel:
        return AnnualTrendsModel.query.filter_by(date=date).first()


    @staticmethod 
    def retrieve_all()-> list[AnnualTrendsModel]:
        return AnnualTrendsModel.query.all()

    @staticmethod
    def delete(source: AnnualTrendsModel) :
        temp =   AnnualTrendsServices.retrieve(source.date)
        if temp:
            db.session.delete(temp)
            db.session.commit()
            
