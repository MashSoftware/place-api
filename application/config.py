import os

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://vagrant:vagrant@localhost:5432/vagrant')
SQLALCHEMY_TRACK_MODIFICATIONS = False
