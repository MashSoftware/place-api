# Mash Place API
[![Build Status](https://travis-ci.org/MashSoftware/place-api.svg?branch=develop)](https://travis-ci.org/MashSoftware/place-api)
[![Requirements Status](https://requires.io/github/MashSoftware/place-api/requirements.svg?branch=master)](https://requires.io/github/MashSoftware/place-api/requirements/?branch=master)

## Getting Started

```
git clone git@github.com:MashSoftware/place-api.git
cd place-api
vagrant up
```

## Post-Installation

```
vagrant ssh
cd /vagrant
export FLASK_APP=mash_place_api/__init__.py
export FLASK_DEBUG=1
sudo su - postgres
createuser -d -E -i -l -P -r -s vagrant
```

Enter password 'vagrant'

```
exit
createdb
psql -c "CREATE EXTENSION postgis;"
```

## Loading Data

Copy Shapefiles into the `/data` directory and then:

```
vagrant ssh
cd /vagrant
./script/load.sh
```

Tables will be created with the name of the shapefile input file. Geometries will be reprojected from the OSGB 1936 / British National Grid (BNG) coordinate reference system (SRID/EPSG: 27700) to WGS84 (SRID/EPSG: 4326), for greater compatibility with GIS products and web mapping libraries. Source data can be obtained from [Ordnance Survey OpenData](https://www.ordnancesurvey.co.uk/business-and-government/products/opendata-products-grid.html) products.

## Running

```
python3 -m flask run --host=0.0.0.0
```
Go to [http://localhost:5000/](http://localhost:5000/)

## Specification

This API is defined using [OpenAPI Specification 2.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) compliant [`swagger.json`](swagger.json) code.

## What's available?
Currently available boundary data is listed here: https://mash-place-api.herokuapp.com/boundaries/

## Mash Place UI
There is an optional user interface available that consumes this API to help with discovering and visualising the data and also as an example of using web mapping tools: [https://github.com/MashSoftware/place-ui](https://github.com/MashSoftware/place-ui)
