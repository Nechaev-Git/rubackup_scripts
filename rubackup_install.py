#!/usr/bin/env python3

import wget
import os
import sys
import subprocess

additional_packages = ["pigz","mailutils","xz-utils","nfs-common","libcurl4","nfs-kernel-server","postgresql","libqt5sql5-psql"]

subprocess.Popen(["sudo","apt","update"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=b'31\n')

for addpack_name in additional_packages:
    print(f'Installing {addpack_name}')
    subprocess.Popen(["sudo","DEBIAN_FRONTEND=noninteractive","apt","-y","install",addpack_name],stdout=subprocess.STDOUT).wait()

packages_path = '/home/u/rubackup-latest/'
packages = ["rubackup-server.deb", "rubackup-client.deb", "rubackup-common.deb", "rubackup-rbm.deb"]

def download_package(package_path, package):
    print(f'Downloading {package}.')
    url = f'http://10.177.32.37:8080/latest/deb/ubuntu/{package}'
    wget.download(url, f'{package_path}{package}')

if os.path.exists(packages_path):
    print(f'{packages_path} is already exist')
else:
    print(f'Creating directory {packages_path}')
    os.mkdir(packages_path)

for package_name in packages:
    if os.path.isfile(packages_path + package_name):
        print(f'Removing {package_name}...')
        os.remove(packages_path + package_name)
        download_package(packages_path, package_name)
    else:
        download_package(packages_path, package_name)





sys.exit(0)