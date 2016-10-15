# Mash Geo API
[![Build Status](https://travis-ci.org/MashSoftware/geo-api.svg?branch=develop)](https://travis-ci.org/MashSoftware/geo-api)

## Getting Started

```
git clone git@github.com:MashSoftware/geo-api.git
vagrant up
```

## Post-Installation

```
vagrant ssh
cd /vagrant
export FLASK_APP=mash_geo_api/__init__.py
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

Geometries will be reprojected from the OSGB 1936 / British National Grid (BNG) coordinate reference system (SRID/EPSG: 27700) to WGS84 (SRID/EPSG: 4326), for greater compatibility with GIS products and web mapping libraries. Source data can be obtained from [Ordnance Survey OpenData](https://www.ordnancesurvey.co.uk/business-and-government/products/opendata-products-grid.html) products.

## Running

```
flask run --host=0.0.0.0
```

## Usage

`GET /constituencies/<ons_code>` Returns a specific Westminster Constituency as a GeoJSON feature:

```
{
  type: "Feature",
  properties: {
    type: "Westminster Constituency",
    name: "Plymouth, Sutton and Devonport Boro Const",
    ons_code: "E14000880",
    hectares: 2261.036
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
