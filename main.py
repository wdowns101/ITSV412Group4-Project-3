import os
import os.path
import requests

path = './http_access_log'

check_file = os.path.isfile(path)

print(check_file)

while (check_file == False):
    print("Downloading the file!")
    downloadUrl = 'https://s3.amazonaws.com/tcmg476/http_access_log'

    req = requests.get(downloadUrl)
    filename = req.url[downloadUrl.rfind('/')+1:]

    with open(filename, 'wb') as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    def download_file(url, filename=''):
        try:
            if filename:
                pass            
            else:
                filename = req.url[downloadUrl.rfind('/')+1:]

            with requests.get(url) as req:
                with open(filename, 'wb') as f:
                    for chunk in req.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                return filename
        except Exception as e:
            print(e)
            return None
        print("File has been downloaded!")
    continue 

print("you have the file!")
