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


install_diri = b"/usr/jcm"


print(text["name"])
install_dir = b''
install_dir = install_diri
install_port = $(bashio::config 'port')
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
fs.write(b"#!/bin/bashio\n")
fs.write(b"cd " + install_dir + b"\n")
fs.write(b"python3 server/jcm.py")
fs.close()
os.system('chmod 777 ' + install_dir.decode("utf-8") + "/run.sh")
user=$(bashio::config 'user')
password=$(bashio::config 'password')

if os.path.exists(".config/main/user") == False:
    if os.path.exists(".config") == False:
        os.mkdir(".config")
    if os.path.exists(".config/main") == False:
        os.mkdir(".config/main")
    print(text["init"])
    user = input(text["user"]).encode("utf-8")
    password = input(text["passwor"]).encode("utf-8")
    tools = imp.load_source('tools',"Tools/Tools.py")
    tools.newuser(user,password,b"0")

os.system('cp -rfv ' + install_dir.decode("utf-8") + "/run.sh /run.sh")