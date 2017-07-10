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

# Requires a directory path as the first argument
if(len(sys.argv) > 1):
    dir = sys.argv[1]
    
    # Check for additional optional argument
    if(len(sys.argv) > 2):
        remove_extensions = True
    else:
        remove_extensions = False

    # Check for files to ignore
    ignore = os.path.join(dir, ign_dir)
    if(os.path.exists(ignore)):
        ignore_patterns_file = os.path.join(ignore, patterns_file)
        if(os.path.exists(ignore_patterns_file)):
            ignore_patterns = open(ignore_patterns_file, "r").read().splitlines()
            has_ignore_patterns = True
    
    # Adapted from: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    categories_path = os.path.join(dir, cat_dir)
    if(os.path.exists(categories_path)):
        has_categories = True
        # Read in categories
        for(dirpath, dirnames, filenames) in walk(categories_path):
            for file in filenames:
                categories[file] = open(os.path.join(categories_path, file)).read().rstrip().split(",")
            break
    
    # Create a list of file names
    files = []
    for(dirpath, dirnames, filenames) in walk(dir):
        files.extend(filenames)
        break

    # Filter out ignored files
    if(has_ignore_patterns):
        files = list(set(files) - set(ignore_patterns))
        files.sort()

    # Check to remove file extensions
    if(remove_extensions):
        for i in range(0, len(files)):
            files[i] = files[i].split(".")[0]
    files = filter(None, files)
    
    # Create a sub-directory at the target path
    target_dir = os.path.join(dir, list_dir);
    if(not os.path.exists(target_dir)):
        os.makedirs(target_dir)
    
    # Write a file listing all the files in the directory
    all = open(os.path.join(target_dir, all_files) + file_ext, 'w+')
    all.write(", ".join(files))
    all.close()
    # For each listed category, write a file listing every file containing a substring in that category
    if(has_categories):
        for key in categories:
            matches = []
            terms = categories[key]
            for i in range(0, len(terms)):
                terms[i] = terms[i].strip()
            for term in terms:
                for file in files:
                    if(term in file):
                        matches.append(file)
            cat_file = open(os.path.join(target_dir, key), 'w+')
            cat_file.write(", ".join(matches))
            cat_file.close()
else:
    print("Please provide target directory")
