# Python File Organizer

## Overview

This Python script provides a simple file organizer that categorizes files based on their types into designated folders. It classifies files into categories such as Images, Videos, Documents, and an "Other" category for files that do not match any predefined types.

## Features

- Organizes files into folders based on their types.
- Creates folders for each file type if they don't already exist.
- Logs the movement of each file to its corresponding folder.

## Usage

1. **Clone the repository:**
```bash
git clone https://github.com/josharsh/100LinesOfCode.git
```

2. **Navigate to the project directory:**
```bash
cd python-file-organizer
```

3. **Run the script:**
```bash
python organizer.py
```
The script will automatically categorize files in the current directory and move them into the appropriate folders.

4. **Check the console output for information about the organization process.**

## Configuration

You can customize the file types and their corresponding folders by modifying the `file_types` dictionary in the `organizer.py` script.

```python
self.file_types = {
 "Image": [".png", '.jpeg', '.jpg'],
 "Video": ['.mp4', '.mkv', '.3gp', '.webp'],
 "Document": ['.pdf', '.doc', '.docx', '.odf', '.odt', '.xlsx'],
 "Other": []
}
```
## Requirements
Python3.x
## Issue and Contributions
Feel free to report any issues or suggest improvements by creating a new issue or submitting a pull request.
