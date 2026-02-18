# Folder Flattener

This script is designed to flatten a directory structure by copying all files from subfolders into a single destination folder. Each file is renamed to include its original folder name to avoid naming conflicts.

## How to use

1. Ensure you have Python installed on your system.
2. Save the `folderflattener.py` script to your desired location.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the command: `python folderflattener.py`.
5. Follow the on-screen prompts to specify the source and destination folders.

## Notes

If you do not specify a destination folder, the script will create a new folder named `flattened_wallpapers` in the current working directory to store the flattened files.

If you do not specify a source folder, the script will use the current working directory as the source.

Naming schema is `<original_folder_name>_<original_file_name>.<extension>`

## Supported file types

The script supports the following image file types: .jpg, .jpeg, .png, .bmp, .gif, .tiff, .tif, .webp
