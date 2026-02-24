# AutoUnzipper

AutoUnzipper is a simple Python script that monitors a directory for new `.zip` files and automatically extracts them to a folder with the same name as the zip file. It uses the `watchdog` library to watch for file system changes and handles common issues like incomplete file writes or permission errors.

## Features

- Automatically extracts new `.zip` files in the monitored directory.
- Waits for the file to be fully written before attempting extraction.

## Usage

1. Install the required library:

   ```bash
   pip install watchdog
   ```

2. Navigate to the directory where you want to monitor for new zip files and place the `main.py` script there.

3. Run the script:

   ```bash
    python main.py
    ```

4. The script will run indefinitely, monitoring for new `.zip` files. When a new zip file is detected, it will attempt to extract it to a folder with the same name as the zip file.

## But why

Why is because I often download zip files and want them to be automatically extracted without having to manually do it every time. This script saves time and effort by automating the extraction process, especially when dealing with multiple zip files.
