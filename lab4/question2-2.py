#How many requests were made on a monthly basis?
import os
import os.path
import datetime
from urllib.request import  urlretrieve #use url.lib


path = './http_access_log.txt'

check_file = os.path.isfile(path) #this is a boolean statement

if (check_file == False):

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

# Initialize a dictionary to store the monthly request counts
monthly_request_counts = {}

# Open the log file and read its contents line by line
with open(path, 'r') as log_file:
    for line in log_file:
        # Split the log entry by space
        parts = line.split()
        if len(parts) >= 10:
            # Extract the date from the log entry 
            date_str = parts[3][1:12]  
          
            if date_str in monthly_request_counts:
                monthly_request_counts[date_str] += 1
            else:
                monthly_request_counts[date_str] = 1

# Print the daily request counts
for date, count in sorted(monthly_request_counts.items()):
    print(f'{date}: {count} requests')
