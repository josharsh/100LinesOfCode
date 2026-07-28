import sys
from PIL import Image
from PIL.ExifTags import TAGS

def extract_exif(image_path):
    try:
        # open image
        image = Image.open(image_path)

        # extract rae EXIF  metadata
        exif_data = image.getexif()

        if not exif_data:
            print("[!] No EXIF metadata found!")
            return

        print(f"\n--- EXIF metadata for : {image_path} ---")

        # iterate through data
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            # filter data
            if isinstance(value, bytes):
                continue
            print(f"{tag_name:<25}: {value}")

    except Exception as e:
        print(f"[ERROR] Could not process image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <IMAGE_PATH>")
    else:
        extract_exif(sys.argv[1])

