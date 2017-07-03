# Author: Isaiah Mann
# Description: Used to list files, separated by comma in a directory

import sys
import os
from os import walk

# Constants
no_ext = "--no-ext"
list_dir = "Listings"
cat_dir = "Categories"
ign_dir = "Ignore"
all_files = "AllFiles"
patterns_file = "Patterns.txt"
file_ext = ".txt"

# Variables
ignore_patterns = []
has_ignore_patterns = False
categories = {}
has_categories = False

if(len(sys.argv) > 1):
    dir = sys.argv[1]
    if(len(sys.argv) > 2):
        remove_extensions = True
    else:
        remove_extensions = False
    ignore = os.path.join(dir, ign_dir)
    if(os.path.exists(ignore)):
        ignore_patterns_file = os.path.join(ignore, patterns_file)
        if(os.path.exists(ignore_patterns_file)):
            ignore_patterns = open(ignore_patterns_file, "r").read().splitlines()
            has_ignore_patterns = True
    # Adapted from: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    files = []
    categories_path = os.path.join(dir, cat_dir)
    if(os.path.exists(categories_path)):
        # Read in categories
        print("TODO: Implement reading in categories")
    for(dirpath, dirnames, filenames) in walk(dir):
        files.extend(filenames)
        break
    if(has_ignore_patterns):
        files = list(set(files) - set(ignore_patterns))
        files.sort()
    if(remove_extensions):
        for i in range(0, len(files)):
            files[i] = files[i].split(".")[0]
    files = filter(None, files)
    target_dir = os.path.join(dir, list_dir);
    if(not os.path.exists(target_dir)):
        os.makedirs(target_dir)
    all = open(os.path.join(target_dir, all_files) + file_ext, 'w+')
    all.write(", ".join(files))
    all.close()
else:
    print("Please provide target directory")
