# Author: Isaiah Mann
# Description: Used to list files, separated by comma in a directory

import sys

# Constants
no_ext = "--no-ext"
list_dir = "Listings"

if(len(sys.argv) > 1):
    dir = sys.argv[1]
else:
    print("Please provide target directory")
