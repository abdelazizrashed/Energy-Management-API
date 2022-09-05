# from cmath import exp
from ..shared.db import db
from ..energy_units.models import EnergyUnitModel


class DriverModel(db.Model):

    __tablename__ = "Drivers"

    # region Columns

    date = db.Column(db.String(50), primary_key=True)
    energy = db.Column(db.Numeric(), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey(
        f'{EnergyUnitModel.__tablename__}.unit_id'), nullable=False)
    expected_demand = db.Column(db.Numeric(), nullable=True)
    intensity_index = db.Column(db.Numeric(), nullable=True)
    difference = db.Column(db.Numeric(), nullable=True)
    cusum = db.Column(db.Numeric(), nullable=True)

    # endregion

    def __init__(self, date, energy, unit_id, expected_demand, intensity_index, difference, cusum,) -> None:
        super().__init__()
        self.date = date
        self.energy = energy
        self.unit_id = unit_id
        self.expected_demand = expected_demand
        self.intensity_index = intensity_index
        self.difference = difference
        self.cusum = cusum

    def to_json(self) -> dict:
        return {
            "date": self.date,
            "energy": str(self.energy),
            "unit_id": str(self.unit_id),
            "expected_demand": str(self.expected_demand),
            "intensity_index":str( self.intensity_index),
            "difference":str( self.difference),
            "cusum": str(self.cusum),
        }

    @staticmethod
    def from_json(data: dict):
        return DriverModel(data["date"], data["energy"], data["unit_id"], data["expected_demand"], data["intensity_index"], data["difference"], data["cusum"])
