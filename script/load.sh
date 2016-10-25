#!/usr/bin/env bash

for f in /vagrant/data/*.shp
do
  basename=$(basename $f)
  filename="${basename%.*}"
  pkey="_pkey"
  echo "--- LOADING SHAPEFILE: $filename ---"
  shp2pgsql -d -I -s 27700:4326 $f $filename | psql -q $DATABASE_URL
  psql $DATABASE_URL -c "ALTER TABLE $filename DROP CONSTRAINT $filename$pkey;"
  psql $DATABASE_URL -c "ALTER TABLE $filename ADD PRIMARY KEY (code);"
  echo "--- COMPLETED LOADING SHAPEFILE: $filename ---"
done
