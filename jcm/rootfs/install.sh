#!/bin/bash
export dir=https://github.com/XiaoXianNv-boot/jcm/releases/download/Preview

#export dir=http://192.168.2.2/data/jcm/pkg

cd /config/jcm/
mkdir -p jcm_install 
cd jcm_install 
mkdir -p Tools 
cd Tools 
curl -#fL -o install.py -C - $dir/install.py 
cd .. 
mkdir -p lib 
cd lib 
mkdir -p pkg 
cd pkg 
curl -#fL -o APP_V0.2.pkg -C - $dir/APP_V0.2.pkg 
curl -#fL -o main_V0.2.pkg -C - $dir/main_V0.2.pkg 
cd .. 
cd .. 
python3 /install.py 
mkdir -p /etc/services.d
mkdir -p /etc/services.d/jcm
chmod 777 /run.sh
chmod 777 /stop.sh
cp /stop.sh /config/jcm/main/stop.sh
ln -s /run.sh /etc/services.d/jcm/run
ln -s /config/jcm/main/stop.sh /etc/services.d/jcm/finish
