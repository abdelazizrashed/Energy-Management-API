from unicodedata import name
from ..shared.db import db
from ..energy_seu.models import EnergySEUModel


class HeatUserModel(db.Model):
    __tablename__ = "HeatUsers"

    id = db.Column(db.Integer, primary_key=True)
    process_type = db.Column(db.String(), db.ForeignKey(
        f'{EnergySEUModel.__tablename__}.type'))
    name_plate = db.Column(db.String())
    vsd_speed = db.Column(db.Numeric())
    load = db.Column(db.Numeric())
    actual_power = db.Column(db.Numeric())
    annual_power = db.Column(db.Numeric())
    note = db.Column(db.String())
    off_times = db.Column(db.String())
    percent_total = db.Column(db.Numeric())
    estimation_process = db.Column(db.String())
    improvments = db.Column(db.String())
    purpose = db.Column(db.String())
    type = db.Column(db.String())
    is_yearly = db.Column(db.Boolean)

    def __init__(self,
                 id,
                 process_type,
                 name_plate,
                 vsd_speed,
                 load,
                 actual_power,
                 annual_power,
                 note,
                 off_times,
                 percent_total,
                 estimation_process,
                 improvments,
                 purpose,
                 type,
                 is_yearly,
                 ) -> None:
        super().__init__()
        self.id = id
        self.process_type = process_type
        self.name_plate = name_plate
        self.vsd_speed = vsd_speed
        self.load = load
        self.actual_power = actual_power
        self.annual_power = annual_power
        self.note = note
        self.off_times = off_times
        self.percent_total = percent_total
        self.estimation_process = estimation_process
        self.improvments = improvments
        self.purpose = purpose
        self.type = type,
        self.is_yearly = is_yearly

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "process_type": self.process_type,
            "name_plate": self.name_plate,
            "vsd_speed": str(self.vsd_speed),
            "load":str( self.load),
            "actual_power": str(self.actual_power),
            "annual_power": str(self.annual_power),
            "note": self.note,
            "off_times": self.off_times,
            "percent_total": str(self.percent_total),
            "estimation_process": self.estimation_process,
            "improvments": self.improvments,
            "purpose": self.purpose,
            "type": self.type,
            "is_yearly": self.is_yearly,
        }

    @staticmethod
    def from_json(data: dict):
        return HeatUserModel(
            data["id"],
            data['process_type'],
            data['name_plate'],
            data['vsd_speed'],
            data['load'],
            data['actual_power'],
            data['annual_power'],
            data['note'],
            data['off_times'],
            data['percent_total'],
            data['estimation_process'],
            data['improvments'],
            data['purpose'],
            data['type'],
            data['is_yearly']
        )
