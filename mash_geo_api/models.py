from mash_geo_api import db
from geoalchemy2 import Geometry
import json


class Constituency(db.Model):
    gid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    area_code = db.Column(db.String(3))
    descriptio = db.Column(db.String(50))
    file_name = db.Column(db.String(50))
    number = db.Column(db.Float(precision=8))
    number0 = db.Column(db.Float(precision=8))
    polygon_id = db.Column(db.Float(precision=8))
    unit_id = db.Column(db.Float(precision=8))
    code = db.Column(db.String(9))
    hectares = db.Column(db.Float(precision=8))
    area = db.Column(db.Float(precision=8))
    type_code = db.Column(db.String(2))
    descript0 = db.Column(db.String(25))
    type_cod0 = db.Column(db.String(3))
    descript1 = db.Column(db.String(36))
    geom = db.Column(Geometry('MULTIPOLYGON'))

    def __init__(self, arg):
        super(Constituency, self).__init__()
        self.arg = arg

    def __repr__(self):
        return json.dumps(
            {"gid": self.gid,
             "name": self.name,
             "area_code": self.area_code,
             "description": self.descriptio,
             "file_name": self.file_name,
             "number": self.number,
             "number_0": self.number0,
             "polygon_id": self.polygon_id,
             "unit_id": self.unit_id,
             "code": self.code,
             "hectares": self.hectares,
             "area": self.area,
             "type_code": self.type_code,
             "description_0": self.descript0,
             "type_code_0": self.type_cod0,
             "description_1": self.descript1},
            sort_keys=True, indent=2
        )
