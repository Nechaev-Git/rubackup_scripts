import wget

packages = ["rubackup-server.deb", "rubackup-client.deb", "rubackup-common.deb", "rubackup-rbm.deb"]

for package_name in packages:
    print(f'Downloading {package_name}...')

    url = f'http://10.177.32.37:8080/latest/deb/ubuntu/{package_name}'
    wget.download(url, f'/home/u/rubackup-latest/{package_name}')

