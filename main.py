import os
import os.path
import requests
from datetime import datetime
from tqdm import tqdm 

path = './http_access_log.txt'

month_mapping = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}     #Month mapping to check number of month and to calculate year

def read_last_line(file_path): #Read the last line of the file
    with open(file_path, 'r') as file:
        for line in file:
            last_line = line  # Store the current line in the variable
    if last_line is not None:
        last_line = last_line.strip()
    else:
        print('File is empty')
    date_str = last_line.split('[')[-1].split(']')[0]
    date_obj = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')
    month = date_obj.strftime('%b')
    year = date_obj.strftime('%Y')
    month_number = month_mapping[month]
    return month_number, year

def check_past_month(month, year, file_path):
    past_six_months = month - 5
    if past_six_months <= 0:              #Handle a case where it could go to last year
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
            if f"{six_months_ago_month_name}/{year}" in line:
                break
    return six_months_ago_month_name, year, line_number

def check_total_requests(file_path):
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
    return line_count

if __name__ == "__main__":
    check_file = os.path.isfile(path)
    if not check_file:
        print("You do not have the file.")
        print("Downloading the file...")

        downloadUrl = 'https://s3.amazonaws.com/tcmg476/http_access_log'
        req = requests.get(downloadUrl, stream=True)  # Use stream=True to download in chunks
        filename = "http_access_log.txt"

        total_size = int(req.headers.get('content-length', 0))

        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

        with open(filename, 'wb') as textfile:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    textfile.write(chunk)
                    progress_bar.update(len(chunk))  

        progress_bar.close()
        
    else:                                   #Else, we already have the file and ready to analyze
        print("You have the file!")
        print("Analyzing data...")

    last_month, last_year = read_last_line(path)                                                                                  #After downloading, read the file and get the most recent month
    six_months_ago_month, six_months_ago_year, six_months_requests = check_past_month(last_month, last_year, path)               #Get which month is the past 6 months and whether it was in the last year or not and get the first line that the 6 month ago started
    total_requests = check_total_requests(path)                                                                                    #Total number of lines in the log should give the total requests in the entire period
    six_months_total_requests = total_requests - six_months_requests     #Subtract the first line number of desired month from total request
    print(f"Total requests in the time period in the log: {total_requests}")
    print(f"Total requests in the past 6 months: {six_months_total_requests}")

