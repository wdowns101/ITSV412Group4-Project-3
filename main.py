import os
import requests

# Define the URL of the file to download
file_url = "https://s3.amazonaws.com/tcmg476/http_access_log"

# Define the path to the "Downloads" folder
downloads_folder = os.path.expanduser("~") + "Users/Downloads/"
