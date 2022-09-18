from ..shared.db import db
from ..energy_units.models import EnergyUnitModel
from ..energy_sources.models import EnergySourceModel
from ..energy_sources.services import EnergySourceServices
from ..energy_units.services import EnergyUnitServices

class MonthlyEnergyConsumtionModel(db.Model):
    __tablename__ = 'MonthlyEnergyConsumtion'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    month = db.Column(db.String(), nullable=False)
    # type = db.Column(db.String(100), nullable=False,primary_key=True)
    cost = db.Column(db.Integer, nullable=False)
    usage = db.Column(db.Integer, nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey(
        f'{EnergyUnitModel.__tablename__}.unit_id'), nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey(
        f'{EnergySourceModel.__tablename__}.source_id'), nullable=False)

        
    def __init__(self, id, month, cost, usage, unit_id, source_id) -> None:
        super().__init__()
        self.id = id
        self.month= month
        self.cost = cost
        self.usage = usage
        self.unit_id = unit_id
        self.source_id = source_id

    def to_json(self) -> dict:
        unit = EnergyUnitServices.retrieve(self.unit_id)
        source = EnergySourceServices.retrieve(self.source_id)
        return {
            "id": self.id,
            "source": source.to_json(),
            "month": self.month,
            "cost":self.cost,
            "usage":self.usage,
            "unit":unit.to_json(),
        }

    @staticmethod
    def from_json(data: dict):
        return MonthlyEnergyConsumtionModel(
            data["id"],
            data['month'], 
            data['cost'], 
            data['usage'], 
            data['unit_id'],
            data["source_id"], 
            )