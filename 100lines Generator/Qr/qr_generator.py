#!/usr/bin/env python3
"""
QR Code Generator Utility

Generates a QR code from user-defined data and saves it as a PNG file
in the user's Downloads folder.

Dependencies:
    pip install qrcode[pil]

Usage:
    python qr_generator.py
"""

import os
import sys
from datetime import datetime
try:
    import qrcode:
except ImportError:
    print("Module 'qrcode' not found. Please install it with: pip install qrcode[pil]")
    sys.exit(1)


def get_downloads_folder():
    """Return the path to the user's Downloads folder in a cross-platform way."""
    if sys.platform.startswith('win'):
        import ctypes.wintypes

        # SHGetKnownFolderPath constants
        CSIDL_PERSONAL = 0x0005  # My Documents
        SHGFP_TYPE_CURRENT = 0
        try:
            from ctypes import windll, create_unicode_buffer

            buf = create_unicode_buffer(260)
            # 0x000c is CSIDL for Downloads folder (CSIDL_DOWNLOADS)
            # Windows Vista and later supports KnownFolder API better but fallback here
            # For simplicity, try the environment variable fallback below instead

            # If this method is unreliable, fallback to env var:
            downloads = os.path.join(os.environ['USERPROFILE'], 'Downloads')
            if os.path.exists(downloads):
                return downloads
        except Exception:
            pass
        # fallback
        return os.path.join(os.path.expanduser('~'), 'Downloads')

    else:
        # macOS and Linux generally have ~/Downloads
        return os.path.join(os.path.expanduser('~'), 'Downloads')


def main():
    print("=== QR Code Generator Utility ===")
    data = input("Enter the data to encode in the QR code: ").strip()

    if not data:
        print("No data entered. Exiting.")
        return

    downloads_path = get_downloads_folder()
    if not os.path.exists(downloads_path):
        print(f"Downloads folder not found at expected location: {downloads_path}")
        print("Saving in current directory instead.")
        downloads_path = os.getcwd()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"qr_code_{timestamp}.png"
    filepath = os.path.join(downloads_path, filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filepath)

    print(f"QR code saved to: {filepath}")


if __name__ == "__main__":
    main()
