# coding=utf-8
#!/bin/python

import os
import sys
import imp
import platform
import shutil
import binascii
import hashlib
import locale

install_diri = b"C:\jcm"
install_porti = 8888
install_booti = b"yes"
pwd = os.getcwd()

text = {}
text["name"] = "# JCM (jiang Cluster Management) Installer#"
text["insdir"] = "install dir: "
text["port"] = "port: "
text["boot"] = "boot: "
text["qr"] = "Confirm the information, enter the exit exit installation"
text["oserr"] = "Get OS name error"
text["init"] = "init"
text["osname"] = "OS Name:"
text["devname"] = "Host Name:"

def pr(new_client_socket,data):
    print(data.decode("utf-8"),end='')

OS_ = platform.system()


install_diri = b"/config/jcm/main"
os.system("mkdir -p /config")
os.system("mkdir -p /config/jcm")
os.system("mkdir -p /config/jcm/main")


print(text["name"])
install_dir = b''
install_dir = install_diri
install_port = install_porti
install_boot = install_booti
print("#############################")
print(text["insdir"] + "" + install_dir.decode("utf-8"))
print(text["port"] + "" + str(install_port))
print(text["boot"] + "" + install_boot.decode("utf-8"))
print("#############################")

OS_ = platform.system()
OS = ''
if os.path.exists('/etc/os-release'):
    sh = os.popen("cat /etc/os-release | grep PRETTY_NAME")
    shell = sh.read().split('"')
    OS = shell[1]
else:
    sh = os.popen("uname -n")
    shell = sh.read()
    OS = shell[:-1]
sh = os.popen('cat /etc/hostname')
dev_name = sh.read().split('\n')[0]
if os.path.exists(install_dir.decode("utf-8") + "") == False:
    os.mkdir(install_dir.decode("utf-8") + "")
if os.path.exists(install_dir.decode("utf-8") + "/server") == False:
    os.mkdir(install_dir.decode("utf-8") + "/server")
if os.path.exists(install_dir.decode("utf-8") + "/Tools") == False:
    os.mkdir(install_dir.decode("utf-8") + "/Tools")
if os.path.exists(install_dir.decode("utf-8") + "/web") == False:
    os.mkdir(install_dir.decode("utf-8") + "/web")
OSs = OS.split(' ')
os.chdir(install_dir.decode("utf-8"))
os.chdir(install_dir.decode("utf-8"))
if os.path.exists(install_dir.decode("utf-8") + "/lib") == False:
    os.mkdir(install_dir.decode("utf-8") + "/lib")
if os.path.exists(install_dir.decode("utf-8") + "/lib/pkg") == False:
    os.mkdir(install_dir.decode("utf-8") + "/lib/pkg")
os.system("cp -rf \"" + pwd + "/lib/pkg\" \"" + install_dir.decode("utf-8") + "/lib\"")
if os.path.exists(install_dir.decode("utf-8") + "/.out") == False:
    os.mkdir(install_dir.decode("utf-8") + "/.out")
print("install main")
os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out")
os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/main_V0.2.pkg")
os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/main_V0.2.pkg/.out")
sh = "tar xzf lib/pkg/main_V0.2.pkg " + "-C .out/main_V0.2.pkg/"
os.system(sh)
sh = install_dir.decode("utf-8") + "/.out/main_V0.2.pkg/.out/server/main/Package.py"
sh = imp.load_source(sh,sh)
sh.install("","","","","",pr)
print("install APP")
os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out")
os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg")
os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg/.out")
sh = "tar xzf lib/pkg/APP_V0.2.pkg " + "-C .out/APP_V0.2.pkg/"
os.system(sh)
sh = install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg/.out/server/APP/Package.py"
sh = imp.load_source(sh,sh)
sh.install("","","","","",pr)

fs = open(install_dir.decode("utf-8") + "/run.sh","wb")
fs.write(b"#!/usr/bin/env bashio\n")
fs.write(b"cd " + install_dir + b"\nbashio::log.info run jcm.py\n")
fs.write(b"python3 -m venv venv\n")
fs.write(b"source ./venv/bin/activate\n")
#fs.write(b"python3 server/jcm.py")
#fs.write(b"python3 server/jcm.py hass $(bashio::config 'port') $(bashio::config 'user') $(bashio::config 'password')")
fs.write(b"python3 server/jcm.py hass 8888 admin admin")
fs.close()
fs = open(install_dir.decode("utf-8") + "/info.sh","wb")
fs.write(b"#!/usr/bin/env bashio\n")
fs.write(b"bashio::log.info $1\n")
fs.close()
fs = open(install_dir.decode("utf-8") + "/error.sh","wb")
fs.write(b"#!/usr/bin/env bashio\n")
fs.write(b"bashio::log.error $1\n")
fs.close()
fs = open(install_dir.decode("utf-8") + "/api.sh","wb")
fs.write(b"#!/usr/bin/env bashio\n")
fs.write(b"bashio::$1 $2\n")
fs.close()
os.system('chmod 777 ' + install_dir.decode("utf-8") + "/api.sh")
os.system('chmod 777 ' + install_dir.decode("utf-8") + "/run.sh")
os.system('chmod 777 ' + install_dir.decode("utf-8") + "/info.sh")
os.system('chmod 777 ' + install_dir.decode("utf-8") + "/error.sh")
os.system('chmod 777 /run.sh')
