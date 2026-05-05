"""Bulk File Renamer
A simple script to bulk rename files in a directory by adding a base filename as a prefix."""
import os

def main():
    """Main function to execute the bulk file renaming process."""
    rootdir = input("Input directory to iterate through. \
Leave blank for current working directory: ")
    if not rootdir:
        rootdir = os.getcwd()
    print(f"{rootdir} selected")

    base_filename = input("Input base file name to use for renaming: \
Leaving blank will result in an underscore being used as the prefix: ")

    for root, _, files in os.walk(rootdir):
        for file in files:
            print(file)
            print(f"{file} renamed to {(base_filename + '' if not base_filename else '_') + file}")
            os.rename(os.path.join(root, file), \
                os.path.join(root, (base_filename + "" if not base_filename else "_") + file))
main()
