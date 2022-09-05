from ..shared.db import db


class EnergyUnitModel(db.Model):
    __tablename__ = "EnergyUnits"

    # region SQLAlchemy table columns

    unit_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # endregion

    def __init__(self, unit_id: int, name: str) -> None:
        super().__init__()
        self.unit_id = unit_id
        self.name = name

    def to_json(self) -> dict:
        return {
            "unit_id": self.unit_id,
            "name": self.name,
        }

    @staticmethod
    def from_json(data: dict):
        return EnergyUnitModel(data["unit_id"], data['name'])
    
    def copy_with(self, unit_id: int, name: str):
        return EnergyUnitModel(unit_id if unit_id else self.unit_id, name if name else self.name);


