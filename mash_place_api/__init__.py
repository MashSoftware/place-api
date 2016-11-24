# flake8: noqa
from flask import Flask
from flask_compress import Compress
from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#App config
app.config.from_pyfile('config.py')

#SQL Alchemy
db = SQLAlchemy(app)

# Flask Compress
Compress(app)

# Flask Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

#Register blueprints
from mash_place_api.general import views as general_views
app.register_blueprint(general_views.general_bp)

from mash_place_api.boundaries import views as boundary_views
app.register_blueprint(boundary_views.boundaries_bp, url_prefix='/boundaries')
