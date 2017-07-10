# File Lister

## Usage
1. Choose a directory within which you want the files listed
2. [OPTIONAL] Create a sub-directory within the target directory labeled "Ignore" and a file within it titled "Ignore.txt." Write any filenames (one per line) you want ignored
3. [OPTIONAL] Create a sub-directory within the target directory labeled "Categories" and create .txt files for each category you want listed. Each text file should contain comma-separated substrings to be located within the filenames
4. Run the program `python file_lister.py [target directory path]. You can add the `--no-ext` argument after the directory path if you want to remove file extensions from the listings.
5. This should produce a sub-directory within the target entitled "Listings." This directory will contain "All.txt" (listing all files) and a text file of files for each specified category
