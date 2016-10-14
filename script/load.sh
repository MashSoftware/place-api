#!/usr/bin/env bash

for f in /vagrant/data/*.shp
do
  echo "--- LOADING SHAPEFILE: $filename ---"
  shp2pgsql -d -I-t 2D -s 27700:4326 $f public.constituency | psql -q $DATABASE_URL
  psql -c "ALTER TABLE public.constituency DROP CONSTRAINT constituency_pkey;"
  psql -c "ALTER TABLE public.constituency ADD PRIMARY KEY (code);"
  echo "--- COMPLETED LOADING SHAPEFILE: $filename ---"
done
