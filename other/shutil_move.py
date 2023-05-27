import shutil
import os

file_source = '/home/rusl4n/Documents/projects/example-code/other/'
file_destination = '/home/rusl4n/Documents/projects/example-code/other/'

get_files = os.listdir(file_source)

for g in get_files:
    shutil.move(file_source + g, file_destination)
