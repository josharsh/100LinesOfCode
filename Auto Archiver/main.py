"""module"""

import os
from datetime import datetime
import shutil

to_archive = []

def cd():
    """Changes the current working directory to the user's Downloads folder."""
    user = os.getlogin()
    os.chdir(f"C:\\Users\\{user}\\Downloads")
    print(os.getcwd())

def main():
    """Main function to list files in the Downloads folder and their last modified times."""
    cd()
    for root, _, files in os.walk(os.getcwd()):
        try:
            for file in files:
                mtime = os.path.getmtime(os.path.join(root, file))
                realmtime = datetime.fromtimestamp(mtime).isoformat()
                if not mtime > (datetime.now().timestamp() - 720 * 3600):
                    print(f"{os.path.join(root, file)} - Last modified: {realmtime} (not modified within the last 30 days)")
                    to_archive.append(os.path.join(root, file))
                # print(f"{file} - Last modified: {realmtime}")
        except OSError as e:
            print(e)
            continue
    print(f"Total files to archive: {len(to_archive)}")
    if input("Do you want to archive these files? (y/n): ").lower() == 'y':
        print("Archiving files...")
        # Ensure the archive directory exists
        archive_dir = os.path.join(os.getcwd(), "Archived")
        try:
            os.makedirs(archive_dir, exist_ok=True)
        except OSError as e:
            print(f"Could not create archive directory {archive_dir}: {e}")
            return
        for file in to_archive:
            try:
                # Preserve the file's relative path under the archive directory
                rel_path = os.path.relpath(file, os.getcwd())
                dst_path = os.path.join(archive_dir, rel_path)
                dst_dir = os.path.dirname(dst_path)
                if dst_dir:
                    os.makedirs(dst_dir, exist_ok=True)
                shutil.copy2(src=file, dst=dst_path)
                print(f"Archived: {file} -> {dst_path}")
            except Exception as e:
                print(f"Error archiving {file}: {e}")

if __name__ == "__main__":
    main()
