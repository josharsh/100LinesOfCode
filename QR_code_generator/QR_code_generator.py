import sys
import time

try:
    import qrcode
    import os
    from pathlib import Path
    from PIL import Image
except ImportError as e:
    print(f"Error: Missing required library: {e.name}")
    print("Please install the required libraries by running:")
    print("pip install qrcode[pil]")
    input("Press Enter to exit...")
    sys.exit(1)

def generate_qr():
    data = input("Enter the text or URL for the QR code: ").strip()
    if not data:
        print("Error: Input cannot be empty.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    downloads_path = str(Path.home() / "Downloads")
    file_name = "generated_qr.png"
    full_path = os.path.join(downloads_path, file_name)

    try:
        img.save(full_path)
        print(f"Success! QR code saved to: {full_path}")
        img.show() 
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        generate_qr()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        input("\nPress Enter to exit...")