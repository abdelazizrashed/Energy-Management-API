from ..shared.db import db
from ..energy_units.models import EnergyUnitModel
from ..energy_sources.models import EnergySourceModel
from ..energy_seu.models import EnergySEUModel

class AnnualTrendsModel(db.Model):
    __tablename__ = "AnnualTrends"
    
    unit_id = db.Column(db.Integer, db.ForeignKey(
        f'{EnergyUnitModel.__tablename__}.unit_id'), nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey(
        f'{EnergySourceModel.__tablename__}.source_id'), nullable=False)
    type = db.Column(db.String(), db.ForeignKey(
        f'{EnergySourceModel.__tablename__}.type'), nullable=False)
    date = db.Column(db.String(), nullable=False)
    consumption = db.Column(db.Numeric(), nullable=False)
    cost = db.Column(db.Numeric(), nullable=False)
    unit_price = db.Column(db.Numeric(), nullable=False)
    budget = db.Column(db.Numeric(), nullable=True)
    target = db.Column(db.Numeric(), nullable=True)

    def __init__(self, unit_id, source_id, type, date, consumption, cost, unit_price, budget, target):
        self.unit_id = unit_id
        self.source_id = source_id
        self.type = type
        self.date = date
        self.consumption = consumption
        self.cost = cost
        self.unit_price = unit_price
        self.budget = budget
        self.target = target


    def to_json(self) -> dict:
        return {
            "source_id": self.source_id,
            "unit_id": self.unit_id,
            "type": self.type,
            "date": self.date,
            "consumption": self.consumption,
            "cost": self.cost,
            "unit_price": self.unit_price,
            "budget": self.budget,
            "target": self.target,
        }

    @staticmethod
    def from_json(data: dict):
        return AnnualTrendsModel(
            data["unit_id"],
            data["source_id"],
            data["type"],
            data["date"],
            data["consumption"],
            data["cost"],
            data["unit_price"],
            data["budget"],
            data["target"],
            )