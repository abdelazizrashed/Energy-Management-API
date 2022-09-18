from ..shared.db import db
from ..energy_units.models import EnergyUnitModel
from ..energy_sources.models import EnergySourceModel
from ..energy_sources.services import EnergySourceServices
from ..energy_units.services import EnergyUnitServices

class MonthlyEnergyConsumtionModel(db.Model):
    __tablename__ = 'MonthlyEnergyConsumtion'
    
    month = db.Column(db.String(), primary_key=True,nullable=False)
    # type = db.Column(db.String(100), nullable=False,primary_key=True)
    cost = db.Column(db.Integer, nullable=False)
    usage = db.Column(db.Integer, nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey(
        f'{EnergyUnitModel.__tablename__}.unit_id'), nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey(
        f'{EnergySourceModel.__tablename__}.source_id'),primary_key=True, nullable=False)

        
    def __init__(self, month, cost, usage, unit_id, source_id) -> None:
        super().__init__()
        self.month= month
        self.cost = cost
        self.usage = usage
        self.unit_id = unit_id
        self.source_id = source_id

    def to_json(self) -> dict:
        unit = EnergyUnitServices.retrieve(self.unit_id)
        source = EnergySourceServices.retrieve(self.source_id)
        return {
            "source": source.to_json(),
            "month": self.month,
            "cost":self.cost,
            "usage":self.usage,
            "unit":unit.to_json(),
        }

    @staticmethod
    def from_json(data: dict):
        return MonthlyEnergyConsumtionModel(
            data['month'], 
            data['cost'], 
            data['usage'], 
            data['unit_id'],
            data["source_id"], 
            )