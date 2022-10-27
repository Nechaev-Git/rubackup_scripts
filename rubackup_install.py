import wget
import os
import sys

packages_path = '/home/u/rubackup-latest/'
packages = ["rubackup-server.deb", "rubackup-client.deb", "rubackup-common.deb", "rubackup-rbm.deb"]

def download_package(package_path, package):
    print(f'Downloading {package}.')
    url = f'http://10.177.32.37:8080/latest/deb/ubuntu/{package}'
    wget.download(url, f'{package_path}{package}')

if os.path.exists(packages_path):
    print(f'{packages_path} is already exist')
else
    os.mkdir(packages_path)

for package_name in packages:
    if os.path.isfile(packages_path + package_name):
        print(f'Removing {package_name}...')
        os.remove(packages_path + package_name)
        download_package(packages_path, package_name)
    else:
        download_package(packages_path, package_name)



sys.exit(0)