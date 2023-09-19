#How many requests were made on a week-by-week basis?
import os
import os.path
from urllib.request import  urlretrieve #use url.lib
from datetime import datetime

path = './http_access_log.txt'

check_file = os.path.isfile(path) #this is a boolean statement

if (check_file == False):

    print("You do not have the file.") #add fetching file
    print("Downloading the file...")

  
# Initialize a dictionary to store the weekly request counts
weekly_request_counts = {}

# Open the log file and read its contents line by line
with open(path, 'r') as log_file:
    for line in log_file:
        # Split the log entry by space
        parts = line.split()
        if len(parts) >= 10:
            # Extract the date from the log entry
            date_str = parts[3][1:12]  # Assuming the date format is [dd/Mon/yyyy:HH]

            # Parse the date string into a datetime object
            log_date = datetime.strptime(date_str, '%d/%b/%Y')

            # Calculate the ISO week number for the date (1-53)
            week_number = log_date.strftime('%G-W%V')

            # Increment the request count for the extracted week
            if week_number in weekly_request_counts:
                weekly_request_counts[week_number] += 1
            else:
                weekly_request_counts[week_number] = 1

# Print the weekly request counts
for week, count in sorted(weekly_request_counts.items()):
    print(f'Week {week}: {count} requests')
