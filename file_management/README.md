# File Management Functions
Useful mass file management functions in Python3. 

These three functions can be used as templates for new functions that meet more specific needs.

## Functions
1. ```replace(to_repl: str, repl: str, path="", walk=False)```:  
    Replaces to_repl string with repl string in file names within folder.


2. ```add_prefix_suffix(fix: str, add_as="prefix", extension="", path="", walk=False)```:  
Add fix string as prefix or suffix before filetype to all files or files with extension if specified.

3. ```collect(key: str, folder_name: str, key_location="contains", extension="", path="")```:  
Move files with key located in filename to folder names folder_name.
Creates folder with folder_name if folder doesn't exist.

## Usage
Download python if not downloaded. Create python file, import functions and call functions.
``` python
from files.py import replace, add_prefix_suffix, collect

# replaces all instances of "new" in file names with "old"
replace(to_repl="new", repl="old", path="/Users/drdre/my_photos")

# adds "_2021" as a suffix to all files with .jpg extension
add_prefix_suffix(fix="_2021", add_as="suffix", extension="jpg", path="/Users/drdre/my_photos")

# collects all files containing "john" in their file name to a new folder named "johns_stuff"
collect(key="john", folder_name="johns_stuff", key_location="contains)
```