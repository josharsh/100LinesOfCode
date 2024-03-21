import os
import shutil


def replace(to_repl: str, repl: str, path="", walk=False) -> None:
    """Replace to_repl string with repl string in all file names.

    Parameters:
        to_repl (str): String being replaced
        repl (str): String to replace with
        path (str): File directory. By default, current directory
        walk (bool): If True, renames files in subfolders also
    """
    if not path:
        path = os.getcwd()

    if walk:
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if not d[0] == "."]
            for filename in files:
                if filename[0] != ".":
                    file, file_extension = os.path.splitext(filename)
                    os.rename(os.path.join(root, filename),
                              os.path.join(root, file.replace(to_repl, repl) + file_extension))
    else:
        for filename in next(os.walk(path))[2]:
            if filename[0] != ".":
                file, file_extension = os.path.splitext(filename)
                os.rename(os.path.join(path, filename),
                          os.path.join(path, file.replace(to_repl, repl) + file_extension))


def add_prefix_suffix(fix: str, add_as="prefix", extension="", path="", walk=False) -> None:
    """Add fix string as prefix or suffix before filetype to all files or files with extension if specified.
    
    Parameters:
        fix (str): String to add as prefix or suffix
        add_as (str): 'prefix' or 'suffix'
        extension (str): Optionally specify file extension of files that can be renamed
        path (str): File directory. By default, current directory
        walk (bool): If True, renames files in subfolders also
    """
    if not path:
        path = os.getcwd()

    if walk:
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if not d[0] == "."]
            for filename in files:
                file, file_extension = os.path.splitext(filename)
                if filename[0] != "." and (file_extension == extension or not extension):
                    if add_as == "prefix":
                        os.rename(os.path.join(root, filename),
                                  os.path.join(root, fix + filename))
                    elif add_as == "suffix":
                        os.rename(os.path.join(root, filename),
                                  os.path.join(root, file + fix + file_extension))

    else:
        for filename in next(os.walk(path))[2]:
            file, file_extension = os.path.splitext(filename)
            if filename[0] != "." and (file_extension == extension or not extension):
                if add_as == "prefix":
                    os.rename(os.path.join(path, filename),
                              os.path.join(path, fix + filename))
                elif add_as == "suffix":
                    os.rename(os.path.join(path, filename),
                              os.path.join(path, file + fix + file_extension))


def collect(key: str, folder_name: str, key_location="contains", extension="", path="") -> None:
    """Move files with key located in filename to folder names folder_name.
    Creates folder with folder_name if folder doesn't exist.

    Parameters:
        key (str): String to check for
        folder_name (str): String specifing folder name to move files into.
        key_location (str): 'contains', 'prefix' or 'suffix'. Specifies location of string. 
        extension (str): Optionally specify file extension of files that can be moved
        path (str): File directory. By default, current directory
    """
    if not path:
        path = os.getcwd()
    if path[-1] == "/":
        path = path[:-1]

    # Add folder if folder doesn't exist
    destination = os.path.join(path, folder_name)
    if not os.path.isdir(destination):
        os.mkdir(destination)

    for filename in next(os.walk(path))[2]:
        if filename[0] != ".":
            file, file_extension = os.path.splitext(filename)
            if file_extension == extension or not extension:
                if (key_location == "contains" and key in file or
                        key_location == "prefix" and file[:len(key)] == key or
                        key_location == "suffix" and file[-len(key):]):
                    shutil.move(os.path.join(path, filename),
                                os.path.join(destination, filename))
