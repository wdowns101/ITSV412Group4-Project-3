import os
import os.path
import requests #use url.lib

'''REMOTE_URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file
'''
path = './http_access_log.txt'

check_file = os.path.isfile(path) #this is a boolean statement

if (check_file == False):

    
    print("You do not have the file.") #add fetching file
'''
    # Fetch the file from the remote server and save it to disk
    print("\n\nDownloading log file from URI... ")
    response = urllib2.urlopen(REMOTE_URL)
    with open(LOCAL_FILE, "wb") as local:
	local.write(response.read())
print "File retrieved and saved to disk (%s) \n\n" % LOCAL_FILE
#else statement here to move on and parse the data
'''
while (check_file != True): #while statement can be replaced with url.lib 

    print("Downloading the file...")
    #The file we want to download
    downloadUrl = 'https://s3.amazonaws.com/tcmg476/http_access_log'

    req = requests.get(downloadUrl)
    filename = "http_access_log.txt"
    #Downloads the file as a .txt file
    with open(filename, 'wb') as textfile:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                textfile.write(chunk)

    def download_file(url, filename=''): #Function that had to be added for this to work for some reason
        try:
            if filename:
                pass            
            else:
                filename = req.url[downloadUrl.rfind('/')+1:]
 
            with requests.get(url) as req:
                with open(filename, 'wb') as textfile:
                    for chunk in req.iter_content(chunk_size=8192):
                        if chunk:
                            textfile.write(chunk)
                return filename
        except Exception as e:
            print(e)
            return None
        print("File has been downloaded!")
    #Looks for the file to close the wile loop
    check_file = os.path.isfile(path)
    print(check_file)

#Verifies that you have the file and will begin analyzing the data
print("You have the file!")
print("Analyzing data...")
with open('http_access_log.txt','r') as file:
   li = file.readlines()
# Define the criteria
criteria = ["May/1995", "Jun/1995", "Jul/1995", "Aug/1995", "Sep/1995", "Oct/1995"]

# Filter and count lines based on the predefined criterias
filtered_lines = [line for line in li if any(keyword in line for keyword in criteria)]
total_lines = len(filtered_lines)

print(f"The number of requests made in the last 6 months: {total_lines}")

total_line = len(li)
print(f"The number of total requests in the log is: {total_line}")

