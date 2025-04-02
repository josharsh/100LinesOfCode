import os
import shutil

def get_extension(file_name):
    """Returns the file extension for a given file name."""
    return file_name.split('.')[-1].lower()

def create_folder(folder_name):
    """Creates a new folder if it doesn't already exist."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")

def move_file(file_name, folder_name):
    """Moves the file to the specified folder."""
    try:
        shutil.move(file_name, folder_name)
        print(f"Moved '{file_name}' to '{folder_name}'")
    except Exception as e:
        print(f"Error moving file '{file_name}': {e}")

def organize_files(directory):
    """Organizes files in the given directory by their file type."""
    os.chdir(directory)
    files = [f for f in os.listdir() if os.path.isfile(f)]

    if not files:
        print("No files to organize in this directory.")
        return

    for file in files:
        extension = get_extension(file)

        if extension in ['jpg', 'jpeg', 'png', 'gif']:
            create_folder('Images')
            move_file(file, 'Images/')
        elif extension in ['pdf', 'docx', 'doc', 'txt']:
            create_folder('Documents')
            move_file(file, 'Documents/')
        elif extension in ['mp4', 'mov', 'avi']:
            create_folder('Videos')
            move_file(file, 'Videos/')
        elif extension in ['mp3', 'wav']:
            create_folder('Music')
            move_file(file, 'Music/')
        else:
            create_folder('Others')
            move_file(file, 'Others/')

def main():
    print("Welcome to File Organizer!")
    directory = input("Enter the directory path you want to organize: ").strip()

    if os.path.isdir(directory):
        organize_files(directory)
    else:
        print("The specified path is not a valid directory.")

if __name__ == "__main__":
    main()
