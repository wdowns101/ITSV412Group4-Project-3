import os
import os.path
import requests
from datetime import datetime

path = './http_access_log.txt'
#Month mapping to check number of month and to calculate year
month_mapping = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr' : 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

#Read the last line of the file
def read_last_line():
    with open(file_path, 'r') as file:
        for line in file:
            last_line = line 
    if last_line is not None:
        last_line = last_line.strip()
    else:
        print('File is empty')
    date_str = last_line.split('[')[-1].split(']')[0]
    date_obj = datetime.striptime(date_sr, %d/%b/%Y:%H:%M:%S %z')
    month = date_obj.strftime('%b')
    year = date_obj.strftime(%Y)
    month_number = month_mapping[month]
    return month_number, year
    

def check_past_month(month, year, file_path):
    past_six_months = month - 5
#Handle a case where it could go to last year
    if past_six_months <= 0:
        past_six_months += 12
        year = year - 1
    for month_name, month_number in month_mapping.items():
        if month_number == past_six_months:
            six_months_ago_month_name = month_name
            break
    with open(file_path, 'r') as file:
        line_number = 0
        for line in file:
            line_number = line_number + 1
            if f"{six_months_agao_month_name}/{year}" in line:
                break
    return six_months_ago_month, year, line_number

#def check_total_requests():
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
