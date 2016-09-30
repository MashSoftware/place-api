#!/usr/bin/env bash

for f in /vagrant/data/*.shp
do
  echo "--- LOADING SHAPEFILE: $filename ---"
  shp2pgsql -d -D -I -s 27700 $f constituency | psql -q $DATABASE_URL
  echo "--- COMPLETED LOADING SHAPEFILE: $filename ---"
done
