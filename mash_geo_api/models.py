from mash_geo_api import db
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely.geometry import mapping
import json

crs = {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::27700"}}


class Constituency(db.Model):
    gid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))  # The name of the boundary.
    area_code = db.Column(db.String(3))  # Code depicting the type of boundary.
    descriptio = db.Column(db.String(50))  # Description of the area_code value.
    file_name = db.Column(db.String(50))  # Name of principle area.
    number = db.Column(db.Float(precision=8))  # Data identifier linked to OS production systems.
    number0 = db.Column(db.Float(precision=8))  # Collection serial number linked to OS production systems.
    polygon_id = db.Column(db.Float(precision=8))  # Global polygon identifier, of use with international boundaries.
    unit_id = db.Column(db.Float(precision=8))  # ID of the admin unit boundary.
    code = db.Column(db.String(9))  # Census code for the given boundary.
    hectares = db.Column(db.Float(precision=8))  # Area in hectares of the boundary.
    area = db.Column(db.Float(precision=8))  # Amount of area which is not considered "in-land".
    type_code = db.Column(db.String(2))  # Code of either VA (Civil Voting Area) or CA (Civil Administration Area).
    descript0 = db.Column(db.String(25))  # Textual description of type_code.
    type_cod0 = db.Column(db.String(3))  # Non-area type code (not currently populated).
    descript1 = db.Column(db.String(36))  # Description of non-area type code (not currently populated).
    geom = db.Column(Geometry('MULTIPOLYGON', srid=27700))

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
             "polygon_id": self.polygon_id,
             "unit_id": self.unit_id,
             "code": self.code,
             "hectares": self.hectares,
             "area": self.area,
             "type_code": self.type_code,
             "description_0": self.descript0,
             "geometry": mapping(to_shape(self.geom)),
             "crs": crs},
            sort_keys=True)
