from ..shared.db import db


class EnergySourceModel(db.Model):
    __tablename__ = "EnergySources"

    # region SQLAlchemy table columns

    source_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # endregion

    def __init__(self, source_id: int, name: str) -> None:
        super().__init__()
        self.source_id = source_id
        self.name = name

    def to_json(self) -> dict:
        return {
            "source_id": self.source_id,
            "name": self.name,
        }

    @staticmethod
    def from_json(data: dict):
        return EnergySourceModel(data["source_id"], data['name'])
    
    def copy_with(self, source_id: int, name: str):
        return EnergySourceModel(source_id if source_id else self.source_id, name if name else self.name);


