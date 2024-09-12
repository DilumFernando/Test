from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)

url = 'http://3dvision.princeton.edu/projects/2014/3DShapeNets/ModelNet10.zip'
save_directory = '/Users/dilumfernando/semester_project'
download_and_unzip(url, save_directory)