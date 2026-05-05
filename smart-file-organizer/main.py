import os
import shutil
from datetime import datetime

# File type mappings
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
}

LOG_FILE = "organizer.log"


def log_action(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")


def create_folder(base_path, folder_name):
    path = os.path.join(base_path, folder_name)
    if not os.path.exists(path):
        os.makedirs(path)
        log_action(f"Created folder: {folder_name}")
    return path


def get_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"


def organize_files(directory):
    if not os.path.exists(directory):
        print("❌ Directory does not exist.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print("📂 No files to organize.")
        return

    for file in files:
        try:
            category = get_category(file)
            category_path = create_folder(directory, category)

            src = os.path.join(directory, file)
            dst = os.path.join(category_path, file)

            # Handle duplicate names
            if os.path.exists(dst):
                name, ext = os.path.splitext(file)
                count = 1
                while os.path.exists(dst):
                    new_name = f"{name}_{count}{ext}"
                    dst = os.path.join(category_path, new_name)
                    count += 1

            shutil.move(src, dst)
            log_action(f"Moved {file} → {category}/")
            print(f"✅ {file} → {category}/")

        except Exception as e:
            log_action(f"Error moving {file}: {str(e)}")
            print(f"⚠️ Error with {file}")


def main():
    print("\n📁 Smart File Organizer")
    print("-" * 30)

    directory = input("Enter folder path to organize: ").strip()

    if not directory:
        print("❌ Please enter a valid path.")
        return

    confirm = input(f"Organize files in '{directory}'? (y/n): ").lower()

    if confirm != "y":
        print("❌ Operation cancelled.")
        return

    organize_files(directory)

    print("\n✨ Done! Check organizer.log for details.\n")


if __name__ == "__main__":
    main()
