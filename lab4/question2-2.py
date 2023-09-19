#How many requests were made on a monthly basis?
from datetime import datetime
import os
import os.path
from urllib.request import urlretrieve  #use url.lib

path = './http_access_log.txt'

check_file = os.path.isfile(path) 

if (check_file is False):

    print("You do not have the file.") #add fetching file
    print("Downloading the file...")
    #The file we want to download
    downloadUrl = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    local_file = 'http_access_log.txt'

    local_file, headers = urlretrieve(downloadUrl,local_file)
    
    print("File has been downloaded!")

    #Verifies that you have the file and will begin analyzing the data
print("You have the file!")
print("Analyzing data...")
with open('http_access_log.txt','r') as file:
    li = file.readlines()

#Store monthly requests
monthly_request_counts = {}

with open(path, 'r') as log_file:
    for line in log_file:
        # Split the log entry by space
        parts = line.split()
        if len(parts) >= 10:
            # Extract the date from the log entry
            date_str = parts[3][1:12] 

            # Parse the date string into a datetime object
            log_date = datetime.strptime(date_str, '%d/%b/%Y')

            # Calculate the year and month for the date
            year_month = (log_date.year, log_date.month)

            # Increment the request count for the extracted month
            if year_month in monthly_request_counts:
                monthly_request_counts[year_month] += 1
            else:
                monthly_request_counts[year_month] = 1

# Print the monthly request counts
for year_month, count in sorted(monthly_request_counts.items()):
    year, month = year_month
    print(f'{year}-{month:02d}: {count} requests')
  
