import requests
import pyspy

def download_file(url, file_name):
    with open(file_name, "wb") as f:
        response = requests.get(url)
        f.write(response.content)


pyspy.run(download_file, 'https://example.com', 'example.html')
