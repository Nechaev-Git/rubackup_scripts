import wget
import os
import sys

packages_path = '/home/u/rubackup-latest/'
packages = ["rubackup-server.deb", "rubackup-client.deb", "rubackup-common.deb", "rubackup-rbm.deb"]

for package_name in packages:
    if os.path.isfile(packages_path + package_name):
        print(f'Removing {package_name}...')
        os.remove(packages_path + package_name)
    else:
        print(f'Downloading {package_name}...')

        url = f'http://10.177.32.37:8080/latest/deb/ubuntu/{package_name}'
        wget.download(url, f'{packages_path}{package_name}')

sys.exit(0)