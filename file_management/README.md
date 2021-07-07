# File Management Functions
Useful mass file management functions in Python3. 

These three functions also make good templates for new functions that meet more specific needs.

## Functions
1. ```replace(to_repl: str, repl: str, path="", walk=False)```:
Replaces to_repl string with repl string in the file names 

2. add_prefix_suffix(fix: str, add_as="prefix", extension="", path="", walk=False):


3. collect(key: str, folder_name: str, key_location="contains", extension="", path="")


## Usage
``` python
from files.py import replace, add_prefix_suffix, collect

# replaces all instances of "new" in file names with "old"
replace(to_repl="new", repl="old", path="/Users/drdre/my_photos")

# adds "_2021" as a suffix to all files with .jpg extension
add_prefix_suffix(fix="_2021", add_as="suffix", extension="jpg", path="/Users/drdre/my_photos")

# collects all files containing "john" in their file name to a new folder named "johns_stuff"
collect(key="john", folder_name="johns_stuff", key_location="contains)
```