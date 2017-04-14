# flake8: noqa
from flask import Flask
from flask_compress import Compress
from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

#App config
app.config.from_pyfile('config.py')

#SQL Alchemy
db = SQLAlchemy(app)

# Flask Compress
Compress(app)

# Flask Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Flask Limiter
limiter = Limiter(app, key_func=get_remote_address, global_limits=["1 per second"])

#Register blueprints
from mash_place_api.general import views as general_views
app.register_blueprint(general_views.general_bp)

from mash_place_api.boundaries import views as boundary_views
app.register_blueprint(boundary_views.boundaries_bp, url_prefix='/v1/boundaries')
