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
flask run --host=0.0.0.0
```
Go to [http://localhost:5000/](http://localhost:5000/)

## Usage

`GET /boundaries/constituencies` - Returns a list of Westminster Constituencies:

```
[
  {
    ons_code: "W07000049",
    name: "Aberavon Co Const"
  },
  {
    ons_code: "W07000058",
    name: "Aberconwy Co Const"
  },
  {...},
  {...}
]
```

`GET /boundaries/constituencies/<ons_code>` - Returns a specific Westminster Constituency as a GeoJSON feature:

```
{
  type: "Feature",
  properties: {
    ons_code: "E14000880",
    name: "Plymouth, Sutton and Devonport Boro Const",
    description: "Westminster Constituency",
    type: "Civil Voting Area",
    hectares: 2261.036,
    attribution: "Contains OS data &copy; Crown copyright and database right (2016)"
  },
  crs: {
    type: "name",
    properties: {
      name: "urn:ogc:def:crs:OGC:1.3:CRS84"
    }
  },
  geometry: {
    type: "MultiPolygon",
    coordinates: [
      [...],
      [...],
      [...]
    ]
  }
}
```

## Mash Place UI
There is an optional user interface available that consumes this API to help with discovering and visualising the data and also as an example of using web mapping tools: [https://github.com/MashSoftware/place-ui](https://github.com/MashSoftware/place-ui)
