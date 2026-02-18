"""module"""
import os
import shutil
from pathlib import Path

def flatten_wallpaper_folders(source_dir, destination_dir):
    """Flattens wallpapers from subfolders in the source directory to the destination directory.
    Each copied file is renamed to include its original folder name to avoid conflicts."""
    valid_extensions = {
        ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".tif", ".webp"
    }

    source_path = Path(source_dir)
    destination_path = Path(destination_dir)
    destination_path.mkdir(parents=True, exist_ok=True)

    copied_count = 0
    error_count = 0

    print(f"\nFlattening wallpapers from:\n{source_path}\n→ {destination_path}\n")
    print("-" * 60)

    for root, _, files in os.walk(source_path):
        current_folder = Path(root)
        if current_folder == source_path:
            continue  # Skip top-level folder

        folder_name = current_folder.name
        for filename in files:
            file_path = current_folder / filename
            if file_path.suffix.lower() not in valid_extensions:
                continue

            new_filename = f"{folder_name}_{file_path.stem}{file_path.suffix}"
            destination_file = destination_path / new_filename

            # Handle name conflicts by appending a counter
            counter = 1
            while destination_file.exists():
                destination_file = destination_path / \
                    f"{folder_name}_{file_path.stem}_{counter}{file_path.suffix}"
                counter += 1

            try:
                shutil.copy2(file_path, destination_file)
                print(f"✓ Copied: {file_path.name} → {destination_file.name}")
                copied_count += 1
            except Exception as e:
                print(f"✗ Error copying {file_path}: {e}")
                error_count += 1

    print("-" * 60)
    print(f"Completed: {copied_count} copied, {error_count} errors.\n")
    return copied_count, error_count


def main():
    """Main function to execute the wallpaper folder flattening process."""
    print("Wallpaper Folder Flattener")
    print("=" * 40)

    source_dir = input("\nEnter the source wallpaper folder: ").strip()
    while not (Path(source_dir).exists() and Path(source_dir).is_dir()):
        source_dir = input("Invalid path. Try again: ").strip()

    destination_dir = input("Enter the destination folder: ").strip()
    if not destination_dir:
        destination_dir = str(Path(source_dir).parent / "Flattened_Wallpapers")

    confirm = input(f"\nProceed copying to '{destination_dir}'? (y/N): ").strip().lower()
    if confirm not in ("y", "yes"):
        print("Operation cancelled.")
        return

    try:
        copied, errors = flatten_wallpaper_folders(source_dir, destination_dir)
        if copied > 0 and errors == 0:
            print("All wallpapers copied successfully.")
        elif copied == 0:
            print("No images found to copy.")
        else:
            print(f"Completed with {errors} errors.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
