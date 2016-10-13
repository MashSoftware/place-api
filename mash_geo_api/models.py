from mash_geo_api import db
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely.geometry import mapping
import json

crs = {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::27700"}}


class Constituency(db.Model):
    gid = db.Column(db.Integer)  # Unique ID from DB sequence.
    name = db.Column(db.String(60))  # The name of the boundary.
    area_code = db.Column(db.String(3))  # Code depicting the type of boundary.
    descriptio = db.Column(db.String(50))  # Description of the area_code value.
    file_name = db.Column(db.String(50))  # Name of principle area.
    number = db.Column(db.Float(precision=8))  # Data identifier linked to OS production systems.
    number0 = db.Column(db.Float(precision=8))  # Collection serial number linked to OS production systems.
    polygon_id = db.Column(db.Float(precision=8))  # Global polygon identifier, of use with international boundaries.
    unit_id = db.Column(db.Float(precision=8))  # ID of the admin unit boundary.
    code = db.Column(db.String(9), primary_key=True)  # Census code for the given boundary.
    hectares = db.Column(db.Float(precision=8))  # Area in hectares of the boundary.
    area = db.Column(db.Float(precision=8))  # Amount of area which is not considered "in-land".
    type_code = db.Column(db.String(2))  # Code of either VA (Civil Voting Area) or CA (Civil Administration Area).
    descript0 = db.Column(db.String(25))  # Textual description of type_code.
    type_cod0 = db.Column(db.String(3))  # Non-area type code (not currently populated).
    descript1 = db.Column(db.String(36))  # Description of non-area type code (not currently populated).
    geom = db.Column(Geometry('MULTIPOLYGON', srid=27700))  # Geometry of the boundary.

    def __init__(self):
        super(Constituency, self).__init__()

    def __repr__(self):
        return json.dumps({"ons_code": self.code,
                           "name": self.name,
                           "type": self.descriptio,
                           "hectares": self.hectares,
                           "crs": crs,
                           "geometry": mapping(to_shape(self.geom))})
