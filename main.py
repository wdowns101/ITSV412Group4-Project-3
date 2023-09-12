import os
import os.path
import requests

from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

path = './http_access_log.txt'

check_file = os.path.isfile(path)

if (check_file == False):
    print("You do not have the file.")

while (check_file != True):

    print("Downloading the file...")
    downloadUrl = 'https://s3.amazonaws.com/tcmg476/http_access_log'

    req = requests.get(downloadUrl)
    filename = "http_access_log.txt"

    with open(filename, 'wb') as textfile:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                textfile.write(chunk)

    def download_file(url, filename=''):
        try:
            if filename:
                pass            
            else:
                filename = req.url[downloadUrl.rfind('/')+1:]

            with requests.get(url) as req:
                with open(filename, 'wb') as textfile:
                    for chunk in req.iter_content(chunk_size=8192):
                        if chunk:
                            textfile.write(chunk)
                return filename
        except Exception as e:
            print(e)
            return None
        print("File has been downloaded!")
    check_file = os.path.isfile(path)
    print(check_file)


print("You have the file!")
print("Analyzing data...")
