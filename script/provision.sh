#!/usr/bin/env bash

echo 'Setting locale...'
sudo locale-gen en_GB.UTF-8

echo 'Installing PostgreSQL & PostGIS...'
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y postgresql-9.6-postgis-2.3 pgadmin3 postgresql-contrib postgis libpq-dev python3-dev

echo 'Installing Pip...'
apt-get -y install python3-pip

echo 'Upgrade Pip...'
pip3 install -U pip

echo 'Installing requirements...'
pip3 install -r /vagrant/requirements.txt
pip3 install -r /vagrant/requirements_test.txt

echo 'Tidying up...'
apt-get autoclean
apt-get -y autoremove

echo 'Done!'
