import os
import os.path
import requests
from datetime import datetime

path = './http_access_log.txt'
#Month mapping to check number of month and to calculate year
month_mapping = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr' : 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
#Read the last line of the file

#Handle a case where it could go to last year

#Calculate total request

if __name__ == "__main__":
    #Check if the log file exists or already been downloaded
    check_file = os.path.isfile(path)
    #If the file doesn't exists, download it and store it in disk space
    if (check_file == False):
        print("You do not have the file.")
        print("Downloading the file...")
        downloadUrl = 'https://s3.amazonaws.com/tcmg476/http_access_log'
        req = requests.get(downloadUrl)
        filename = "http_access_log.txt"
        with open(filename, 'wb') as textfile:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    textfile.write(chunk)
    #Else, we already have the file and ready to anaylze
    else:
        Print("You have the file!")
        Print("Analyzing data.....)
