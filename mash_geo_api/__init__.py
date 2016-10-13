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
from mash_geo_api.views import general, constituencies
app.register_blueprint(general.general_bp)
app.register_blueprint(constituencies.constituencies_bp, url_prefix='/constituencies')
