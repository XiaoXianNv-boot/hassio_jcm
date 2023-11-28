#!/usr/bin/env bashio

if [ -e /config/jcm/main/run.sh ]; then
  bashio /config/jcm/main/run.sh
else
    cd /tmp && \
    mkdir -p jcm_install && \
    cd jcm_install && \
    mkdir -p Tools && \
    cd Tools && \
    curl -#fL -o install.py -C - https://github.com/XiaoXianNv-boot/jcm/releases/download/Preview/install.py && \
    cd .. && \
    mkdir -p lib && \
    cd lib && \
    mkdir -p pkg && \
    cd pkg && \
    curl -#fL -o APP_V0.2.pkg -C - https://github.com/XiaoXianNv-boot/jcm/releases/download/Preview/APP_V0.2.pkg && \
    curl -#fL -o main_V0.2.pkg -C - https://github.com/XiaoXianNv-boot/jcm/releases/download/Preview/main_V0.2.pkg && \
    cd .. && \
    cd .. && \
    python3 /install.py
    mkdir -p /config/jcm/dist-packages
    mkdir -p /config/jcm/lists
    apt remove -y --no-install-recommends python3 gcc wget python3-pip python3-dev
    apt update
    apt install -y --no-install-recommends python3 gcc wget python3-pip python3-dev
    bashio /config/jcm/main/run.sh
fi
