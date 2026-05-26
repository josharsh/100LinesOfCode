# Bulk File Renamer

A simple Python script that allows you to rename multiple files in a directory based on a specified pattern. This script is useful for organizing and managing large collections of files, such as photos, documents, or music.

## How to use

1. Clone the repository or download the `main.py` script.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the following command:

   ```bash
   python main.py
   ```

4. Follow the onscreen prompts.

## Example

If the selected folder contains `image.jpg` and you enter `holiday` as the base file name,
the script renames it to `holiday_image.jpg`. When a target file already exists, a numeric
suffix is added, such as `holiday_image_1.jpg`, so existing files are not overwritten.
