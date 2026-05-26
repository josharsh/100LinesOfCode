"""Bulk File Renamer
A simple script to bulk rename files in a directory by adding a base filename as a prefix."""
import os
from pathlib import Path


def build_new_name(file_path, prefix):
    """Build the renamed file name while preserving the original extension."""
    if file_path.name.startswith(prefix):
        return file_path.name
    return f"{prefix}{file_path.name}"


def unique_destination(file_path, new_name):
    """Return a destination path that does not overwrite an existing file."""
    destination = file_path.with_name(new_name)
    if not destination.exists() or destination == file_path:
        return destination

    stem = destination.stem
    suffix = destination.suffix
    counter = 1
    while True:
        candidate = destination.with_name(f"{stem}_{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def main():
    """Main function to execute the bulk file renaming process."""
    rootdir = input("Input directory to iterate through. \
Leave blank for current working directory: ")
    if not rootdir:
        rootdir = os.getcwd()

    root_path = Path(rootdir).expanduser().resolve()
    if not root_path.is_dir():
        print(f"{root_path} is not a valid directory.")
        return

    print(f"{root_path} selected")

    base_filename = input("Input base file name to use for renaming: \
Leaving blank will result in an underscore being used as the prefix: ").strip()
    prefix = f"{base_filename}_" if base_filename else "_"

    for root, _, files in os.walk(root_path):
        for file in files:
            file_path = Path(root) / file
            new_name = build_new_name(file_path, prefix)
            destination = unique_destination(file_path, new_name)

            if destination == file_path:
                print(f"{file_path.name} already has the prefix; skipped")
                continue

            print(f"{file_path.name} renamed to {destination.name}")
            file_path.rename(destination)


if __name__ == "__main__":
    main()
