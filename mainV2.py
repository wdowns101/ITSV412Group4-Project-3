
import os
import os.path
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
    
# Define the criteria
criteria0 = ["May/1995", "Jun/1995", "Jul/1995", "Aug/1995", "Sep/1995", "Oct/1995"]
criteria3 = ["404","403"]
criteria4 = ["304","303"]

# Python0 Filter and count lines based on the predefined criterias 
filtered_lines = [line for line in li if any(keyword in line for keyword in criteria0)]
total_lines = len(filtered_lines)

# Project404 Filter and count lines based on the predefined criterias 
filtered_lines = [line for line in li if any(keyword in line for keyword in criteria3)]
failed_lines = len(filtered_lines)
percent_failed = round((failed_lines/len(li))*100,2)

filtered_lines = [line for line in li if any(keyword in line for keyword in criteria4)]
redirected_lines = len(filtered_lines)
percent_redirected = round((redirected_lines/len(li))*100,2)


file_counts = {}
for line in li:
    parts = line.split()
    if len(parts) > 6:
        requested_file = parts[6]
        # Check if the requested file exists in the dictionary, if not, initialize it with 1, else increment the count
        if requested_file in file_counts:
            file_counts[requested_file] += 1
        else:
            file_counts[requested_file] = 1

# Find the most and least requested files
most_requested_file = max(file_counts, key=file_counts.get)
most_requested_file_count = file_counts[most_requested_file]
least_requested_file = min(file_counts, key=file_counts.get)
least_requested_file_count = file_counts[least_requested_file]




print(f"The number of requests made in the last 6 months: {total_lines}")

total_line = len(li)
print(f"The number of total requests in the log is: {total_line}")

print(f"The percentage of failed requests is: {percent_failed}" + "%")

print(f"The percentage of redirected requests is: {percent_redirected}" + "%")

print(f"The most requested file is: {most_requested_file} being requested {most_requested_file_count} times.")

print(f"The least requested file is: {least_requested_file} being requested {least_requested_file_count} times.")
