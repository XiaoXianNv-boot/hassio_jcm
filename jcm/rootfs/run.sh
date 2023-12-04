#!/usr/bin/env bashio

if [ -e /config/jcm/main/run.sh ]; then
  bashio::log.info boot
  bashio /config/jcm/main/run.sh
else
  bashio::log.info install
    cd / &&
    tar xvf jcm.tar.gz
    bashio /config/jcm/main/run.sh
fi
