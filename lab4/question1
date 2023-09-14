# How many requests were made on each day?
'''REMOTE_URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file
'''
path = './http_access_log.txt'

# Initialize a dictionary to store the daily request counts
daily_request_counts = {}

# Open the log file and read its contents line by line
with open(path, 'r') as log_file:
    for line in log_file:
        # Split the log entry by space
        parts = line.split()
        if len(parts) >= 4:
            # Extract the date from the log entry (assuming it's in the fourth position)
            date_str = parts[3][1:12]  # Assuming the date format is [dd/Mon/yyyy:HH]
           
# Increment the request count for the extracted date
            if date_str in daily_request_counts:
                daily_request_counts[date_str] += 1
            else:
                daily_request_counts[date_str] = 1

# Print the daily request counts
for date, count in sorted(daily_request_counts.items()):
    print(f'{date}: {count} requests')
