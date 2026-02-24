"""A simple file system watcher that listens for new files in the
current directory and performs actions based on the file type.
This example uses the watchdog library to monitor the file system for changes.
When a new file is created, it checks if the file is a .zip file and
extracts it to a folder with the same name as the zip file.
To run this code, you need to install the watchdog library"""

import os
import time
import zipfile
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

def wait_for_stable_file(path, stable_seconds=1.0, timeout=30.0, poll_interval=0.5):
    """Wait until file size is stable for `stable_seconds` or until timeout.
    Returns True if the file became stable, False on timeout.
    """
    start = time.time()
    last_size = -1
    last_change_time = time.time()
    while True:
        try:
            size = os.path.getsize(path)
        except OSError:
            # File may not exist yet
            size = -1
        now = time.time()
        if size != last_size:
            last_size = size
            last_change_time = now
        if size >= 0 and (now - last_change_time) >= stable_seconds:
            return True
        if (now - start) > timeout:
            return False
        time.sleep(poll_interval)

def try_extract_zip(path, target_dir=None, attempts=6, delay=1.0):
    """Try to extract a zip with retries on PermissionError/BadZipFile/OSError.
    Returns True on success, False otherwise."""
    if target_dir is None:
        target_dir = os.path.splitext(path)[0]
    for attempt in range(1, attempts + 1):
        try:
            with zipfile.ZipFile(path, "r") as z:
                z.extractall(target_dir)
            print(f"Extracted {path} to {target_dir}")
            return True
        except (PermissionError, OSError) as e:
            print(f"Attempt {attempt}: permission/OS error for {path}: {e}")
        except zipfile.BadZipFile as e:
            print(f"Attempt {attempt}: bad zip (likely incomplete) for {path}: {e}")
        if attempt < attempts:
            time.sleep(delay)
    return False

class MyEventHandler(FileSystemEventHandler):
    """Custom event handler that reacts to file creation events."""
    def on_created(self, event):
        # Ignore directory creation events
        if getattr(event, "is_directory", False):
            return
        src = event.src_path
        print(f"File created: {src}")

        # Example action: if a .zip is created, extract it to a folder next to the zip
        if src.lower().endswith(".zip"):
            # Wait for file write to finish (size stable) before extracting
            stable = wait_for_stable_file(src, stable_seconds=1.0, timeout=30.0, poll_interval=0.5)
            if not stable:
                print(f"Time out waiting for {src} to become stable; will still attempt extraction")

            ok = try_extract_zip(src, attempts=8, delay=1.0)
            if not ok:
                print(f"Failed to extract {src} after multiple attempts")

def main():
    """Set up the file system watcher and start monitoring."""
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()
