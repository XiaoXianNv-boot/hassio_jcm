#!/usr/bin/env bashio

if [ -e /config/jcm/main/run.sh ]; then
  bashio /config/jcm/main/run.sh
else
    cd / &&
    tar xvf jcm.tar.gz
    bashio /config/jcm/main/run.sh
fi
