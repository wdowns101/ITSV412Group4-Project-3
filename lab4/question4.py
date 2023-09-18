#3XX redirected
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
criteria = ["304","303"]

# Filter and count lines based on the predefined criterias
filtered_lines = [line for line in li if any(keyword in line for keyword in criteria)]
redirected_lines = len(filtered_lines)
percent_redirected = round((redirected_lines/len(li))*100,2)
print(f"The percentage of redirected requests is: {percent_redirected}" + "%")
