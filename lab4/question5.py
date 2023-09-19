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

# Find the most requested file
most_requested_file = max(file_counts, key=file_counts.get)
most_requested_file_count = file_counts[most_requested_file]
print(f"The most requested file is: {most_requested_file} being requested {most_requested_file_count} times.")
