from ..shared.db import db
from ..energy_sources.models import EnergySourceModel

class EnergySEUModel(db.Model):
    __tablename__ = "EnergySEU"

    
    type = db.Column(db.String(), primary_key=True)
    
    main_driver = db.Column(db.String(50), nullable=False)
    meter_type = db.Column(db.String(50), nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey(
        f'{EnergySourceModel.__tablename__}.source_id'), nullable=False)
    objective = db.Column(db.String(150), nullable=False)
    influencer = db.Column(db.String(150), nullable=False)
    
    target = db.Column(db.Numeric(), nullable=False)
    wpa = db.Column(db.Numeric(), nullable=False)

    def __init__(self, type, main_driver, meter_type, source_id, objective, influencer, target, wpa) -> None:
        super().__init__()
        self.type = type
        self.main_driver = main_driver
        self.source_id = source_id
        self.meter_type = meter_type
        self.objective = objective
        self.influencer = influencer
        self.target = target
        self.wpa = wpa

    def to_json(self) -> dict:
        return {
            "type": self.type,
            "main_driver": self.main_driver,
            "source_id": self.source_id,
            "meter_type": self.meter_type,
            "objective": self.objective,
            "influencer": self.influencer,
            "target": str(self.target),
            "wpa": str(self.wpa),
        }

    @staticmethod
    def from_json(data: dict):
        return EnergySEUModel(
            data.get("type"), 
            data.get('main_driver'),
            data.get('meter_type'),
            data.get('source_id'),
            data.get('objective'),
            data.get('influencer'),
            data.get('target'),
            data.get("wpa"),
            )




