from ..shared.db import db
from ..energy_seu.models import EnergySEUModel


class LightingModel(db.Model):
    __tablename__ = "Lighting"

    id = db.Column(db.Integer, primary_key=True)
    process_type = db.Column(db.String(), db.ForeignKey(
        f'{EnergySEUModel.__tablename__}.type'))
    area = db.Column(db.String())
    category = db.Column(db.String())
    fitting_type = db.Column(db.String())
    fitting_no = db.Column(db.Numeric())
    lamp_rating = db.Column(db.Numeric())
    lamp_no = db.Column(db.Numeric())
    hours_per_year = db.Column(db.Numeric())
    kwh_per_year = db.Column(db.Numeric())
    light_control = db.Column(db.String())
    improvments = db.Column(db.String())
    lux_levels_available = db.Column(db.String())
    required_lux_level = db.Column(db.Numeric())
    actual_lux_level = db.Column(db.Numeric())
    natural_lighting = db.Column(db.String())
    month = db.Column(db.String())

    def __init__(
        self,
        id,
        process_type,
        area,
        category,
        fitting_type,
        fitting_no,
        lamp_rating,
        lamp_no,
        hours_per_year,
        kwh_per_year,
        light_control,
        improvments,
        lux_levels_available,
        required_lux_level,
        actual_lux_level,
        natural_lighting,
        month,
    ) -> None:
        super().__init__()
        self.id = id
        self.process_type = process_type
        self.area = area
        self.category = category
        self.fitting_type = fitting_type
        self.fitting_no = fitting_no
        self.lamp_rating = lamp_rating
        self.lamp_no = lamp_no
        self.hours_per_year = hours_per_year
        self.kwh_per_year = kwh_per_year
        self.light_control = light_control
        self.improvments = improvments
        self.lux_levels_available = lux_levels_available
        self.required_lux_level = required_lux_level
        self.actual_lux_level = actual_lux_level
        self.natural_lighting = natural_lighting
        self.month = month

    def to_json(self) -> dict:
        return {
        "id":self.id,
        "process_type":self.process_type,
        "area":self.area,
        "category":self.category,
        "fitting_type":self.fitting_type,
        "fitting_no":str(self.fitting_no),
        "lamp_rating":str(self.lamp_rating),
        "lamp_no":str(self.lamp_no),
        "hours_per_year":str(self.hours_per_year),
        "kwh_per_year":str(self.kwh_per_year),
        "light_control":self.light_control,
        "improvments":self.improvments,
        "lux_levels_available":self.lux_levels_available,
        "required_lux_level":str(self.required_lux_level),
        "actual_lux_level":str(self.actual_lux_level),
        "natural_lighting":self.natural_lighting,
        "month":self.month,
        }

    @staticmethod
    def from_json(data: dict):
        return LightingModel(
        data["id"],
        data["process_type"],
        data["area"],
        data["category"],
        data["fitting_type"],
        data["fitting_no"],
        data["lamp_rating"],
        data["lamp_no"],
        data["hours_per_year"],
        data["kwh_per_year"],
        data["light_control"],
        data["improvments"],
        data["lux_levels_available"],
        data["required_lux_level"],
        data["actual_lux_level"],
        data["natural_lighting"],
        data["month"],
            )
