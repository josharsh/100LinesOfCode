import os

class Organizer:
    def __init__(self) -> None:
        self.files = [f for f in os.listdir() if os.path.isfile(f)]
        self.file_types = {
            "Image": [".png", '.jpeg', '.jpg'],
            "Video": ['.mp4', '.mkv', '.3gp', '.webp'],
            "Document": ['.pdf', '.doc', '.docx', '.odf', '.odt', '.xlsx'],
            "Other": []
        }

    def check_folders(self) -> None:
        try:
            for folder in self.file_types.keys():
                if not os.path.exists(folder):
                    os.makedirs(folder)
                    print(f"{folder} folder created.")
        except Exception as e:
            print(f"Error while checking and creating folders: {e}")

    def organize_files(self) -> str:
        try:
            for file in self.files:
                for file_type, extensions in self.file_types.items():
                    if any(file.endswith(extension) for extension in extensions):
                        os.rename(file, os.path.join(file_type, file))
                        print(f"Moved {file} to {file_type} folder.")

            remaining_files = [f for f in os.listdir() if os.path.isfile(f)]
            if remaining_files:
                for file in remaining_files:
                    os.rename(file, os.path.join("Other", file))
                    print(f"Moved {file} to Other folder.")

            return "Organized"
        except Exception as e:
            print(f"Error while organizing files: {e}")
            return "Not Organized completely"

    def run(self) -> str:
        self.check_folders()
        status = self.organize_files()
        return status

if __name__ == "__main__":
    PyFO = Organizer()
    is_complete = PyFO.run()
    print(is_complete)
