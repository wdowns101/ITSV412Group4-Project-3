#How many requests were made on a week-by-week basis? Per month?
'''REMOTE_URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file
'''
path = './http_access_log.txt'

weekly_request_counts = {}

# Open the log file and read its contents line by line
with open(path, 'r') as log_file:
    for line in log_file:
        # Split the log entry by space
        parts = line.split()
        if len(parts) >= 10:
            # Extract the date from the log entry 
            date_str = parts[3][1:12]  #
