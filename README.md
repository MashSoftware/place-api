# Mash Geo API
[![Build Status](https://travis-ci.org/MashSoftware/geo-api.svg?branch=develop)](https://travis-ci.org/MashSoftware/geo-api)

## Getting Started

```
export FLASK_APP=mash_geo_api/__init__.py
export FLASK_DEBUG=1
```

## Post-Installation

```
vagrant ssh
sudo su - postgres
createuser -d -E -i -l -P -r -s vagrant
exit
createdb
psql -c "CREATE EXTENSION postgis;"
psql -c "CREATE EXTENSION postgis_topology;"
psql -c "CREATE EXTENSION fuzzystrmatch;"
psql -c "CREATE EXTENSION address_standardizer;"

```

## Loading Data

Copy Shapefiles into the `/data` directory and then:

```
vagrant ssh
cd /vagrant
./script/load.sh
```

The `shp2pgsql` utility is set to import data in the British National Grid (BNG) coordinate reference system (SRID:27700), for example [Ordnance Survey OpenData](https://www.ordnancesurvey.co.uk/business-and-government/products/opendata-products-grid.html) products.

## Running

```
flask run --host=0.0.0.0
```

## Usage

`GET /constituencies` Returns a list of constituencies

`GET /constituencies/<id>` Returns a specific constituency
