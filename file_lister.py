# Author: Isaiah Mann
# Description: Used to list files, separated by comma in a directory

import sys
from os import walk

# Constants
no_ext = "--no-ext"
list_dir = "Listings"

if(len(sys.argv) > 1):
    dir = sys.argv[1]
    if(len(sys.argv) > 2):
        remove_extensions = True
    else:
        remove_extensions
    # Adapted from: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    files = []
    for(dirpath, dirnames, filenames) in walk(dir):
        files.extend(filenames)
        break
    for i in range(0, len(files)):
        files[i] = files[i].split(".")[0]
    print(files)
else:
    print("Please provide target directory")
