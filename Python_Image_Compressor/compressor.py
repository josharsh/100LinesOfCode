import os
from PIL import Image

def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T"]:
        if b < factor: return f"{b:.2f}{unit}{suffix}"
        b /= factor

def compress_img(file_path, quality=60):
    old_size = os.path.getsize(file_path)
    img = Image.open(file_path)
    name, ext = os.path.splitext(file_path)
    new_filename = f"{name}_compressed.jpg"
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(new_filename, "JPEG", optimize=True, quality=quality)
    new_size = os.path.getsize(new_filename)
    percent = ((old_size - new_size) / old_size) * 100
    print(f"File: {os.path.basename(file_path)}")
    print(f"Size: {get_size_format(old_size)} -> {get_size_format(new_size)}")
    print(f"Saved: {percent:.2f}%\n")

if __name__ == "__main__":
    path = input("Enter image path or folder: ").strip('"')
    if os.path.isfile(path):
        compress_img(path)
    elif os.path.isdir(path):
        for file in os.listdir(path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                compress_img(os.path.join(path, file))
    else:
        print("Invalid path!")