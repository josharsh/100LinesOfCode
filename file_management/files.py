import os
import shutil


def replace(to_repl: str, repl: str, path="", walk=False):
    """Replace to_repl string with repl string in all file names.

    Ignores hidden files and folders.
    """
    if not path:
        path = os.getcwd()

    if walk:
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if not d[0] == "."]
            for filename in files:
                if filename[0] != ".":
                    file, file_extension = os.path.splitext(filename)
                    os.rename(
                                os.path.join(root, filename),
                                os.path.join(root, file.replace(to_repl, repl) + file_extension))
    else:
        for filename in next(os.walk(path))[2]:
            if filename[0] != ".":
                file, file_extension = os.path.splitext(filename)
                os.rename(
                            os.path.join(path, filename),
                            os.path.join(path, file.replace(to_repl, repl) + file_extension))


def add_prefix_suffix(fix: str, add_as="prefix", extension="", path="", walk=False):
    """Add string as prefix or suffix before filetype to
    all files or files with extension if specified.
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
                        os.rename(
                                    os.path.join(root, filename),
                                    os.path.join(root, fix + filename))
                    elif add_as == "suffix":
                        os.rename(
                                    os.path.join(root, filename),
                                    os.path.join(root, file + fix + file_extension))

    else:
        for filename in next(os.walk(path))[2]:
            file, file_extension = os.path.splitext(filename)
            if filename[0] != "." and (file_extension == extension or not extension):
                if add_as == "prefix":
                    os.rename(
                                os.path.join(path, filename),
                                os.path.join(path, fix + filename))
                elif add_as == "suffix":
                    os.rename(
                                os.path.join(path, filename),
                                os.path.join(path, file + fix + file_extension))


def collect(key: str, folder_name: str, key_location="contains", extension="", path=""):
    """
    Moves files with key located in filename to folder names folder_name.
    Create folder with folder_name if folder doesn't exist.

    key_location: contains, prefix, suffix
    """
    if not path:
        path = os.getcwd()
    if path[-1] == "/":
        path = path[:-1]

    # Add folder if folder doesn't exist
    destination = os.path.join(path, folder_name)
    os.mkdir(destination)

    for filename in next(os.walk(path))[2]:
        if filename[0] != ".":
            file, file_extension = os.path.splitext(filename)
            if file_extension == extension or not extension:
                if (key_location == "contains" and key in file or
                        key_location == "prefix" and file[:len(key)] == key or
                        key_location == "suffix" and file[-len(key):]):
                    shutil.move(
                                os.path.join(path, file),
                                os.path.join(destination, file))

