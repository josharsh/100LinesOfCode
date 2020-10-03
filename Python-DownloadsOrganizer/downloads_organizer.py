import shutil
import time
from pathlib import Path
from datetime import datetime, timedelta
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from file_extensions import file_formats, EXTENSIONS

DOWNLOADS = Path.home().joinpath("Downloads") # Path to Downloads folder

class DownloadsObserver(FileSystemEventHandler):

    def on_modified(self, event):
        if self.is_download_finished():
            time.sleep(2)  # wait to allow file to be fully written
            self.start_file_organiser()

    def is_download_finished(self):
        firefox_temp_file = sorted(Path(DOWNLOADS).glob('*.part')) # Firefox download parts
        chrome_temp_file = sorted(Path(DOWNLOADS).glob('*.crdownload')) # Chrome download parts
        downloaded_files = sorted(Path(DOWNLOADS).glob('*.*'))

        if len(firefox_temp_file) == 0 \
                and len(chrome_temp_file) == 0 \
                and len(downloaded_files) >= 1:
            return True # The lengths become 0 when the parts combine to become a single file
        else:
            return False

    def start_file_organiser(self):
        for file_name in os.listdir(DOWNLOADS):

            source = DOWNLOADS.joinpath(file_name)
            exten = Path(file_name).suffix  # Get Extension

            if Path(source).is_dir() and file_name not in EXTENSIONS.keys():
                exten_folder_path = DOWNLOADS.joinpath("Folders")
                self.mkdir_and_move(
                    file_name, exten, source, exten_folder_path)

            if Path(source).is_file() and (exten != ".part" or exten != ".crdownload"):
                exten_folder_path = DOWNLOADS.joinpath(file_formats[exten])
                self.mkdir_and_move(
                    file_name, exten, source, exten_folder_path)

    def mkdir_and_move(self, file_name, exten, source, exten_folder_path):
        exten_folder_path.mkdir(exist_ok=True)
        destination = exten_folder_path.joinpath(file_name)
        if Path(destination).exists():
            new_file_path = self.check_file_exists(destination, exten)
            shutil.move(source, new_file_path)
        else:
            shutil.move(source, destination)

    def check_file_exists(self, destination, exten):
        file_without_exten = Path(destination).with_suffix("")
        if Path(destination).exists():
            file_renamed_path = Path(
                str(file_without_exten) + "(copy)" + exten)
            return self.check_file_exists(file_renamed_path, exten)
        else:
            return destination

downloads_event_observer = DownloadsObserver()
downloads_event_observer.start_file_organiser()
observer = Observer()
observer.schedule(downloads_event_observer, DOWNLOADS, recursive=False)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Stopped Observing Downloads")
    observer.stop()
observer.join()