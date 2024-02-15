#!/usr/bin/env bashio

if [ -e /config/jcm/main/run.sh ]; then
  bashio::log.info boot
  bashio /config/jcm/main/run.sh
else
  bashio::log.info install
  mkdir -p /config
  mkdir -p /config/jcm
  cd /config/jcm/
  mkdir -p jcm_install
  cd jcm_install
  curl -#fL -o install.sh -C - https://github.com/XiaoXianNv-boot/jcm/raw/master/Tools/install.sh
  bashio::log.info DOW EN
  if [ -e install.sh ]; then
    bashio::log.info run install bash
    bash install.sh
    bashio::log.info install ok
  else
    #Replace the source
    bashio::log.info GitHub Down ERROR
    curl -#fL -o install.sh -C - https://jiang144.i234.me/data/jcm/install/install.sh
    bashio::log.info DOW EN
    if [ -e install.sh ]; then
      bashio::log.info run install bash
      bash install.sh
      bashio::log.info install ok
    else
      bashio::log.info GitHub Down ERROR
      echo 网络错误,无法下载安装脚本,请检查网络
      echo Network error, unable to download installation script, please check the network
      exit 1
    fi
  fi
    bashio /config/jcm/main/run.sh
fi
