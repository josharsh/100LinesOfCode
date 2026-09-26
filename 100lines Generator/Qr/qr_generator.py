#!/usr/bin/env python3
"""Generate a QR code from user input and save it as a PNG image."""

from datetime import datetime
from pathlib import Path

try:
    import qrcode
except ImportError:
    print("Module 'qrcode' not found. Please install it with: pip install qrcode[pil]")
    raise SystemExit(1)


def get_downloads_folder():
    """Return the user's Downloads folder, creating it when necessary."""
    downloads = Path.home() / "Downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    return downloads


def generate_qr(data):
    """Create a PNG QR code and return its path."""
    if not data.strip():
        raise ValueError("Data cannot be empty.")

    filename = f"qr_code_{datetime.now():%Y%m%d_%H%M%S}.png"
    filepath = get_downloads_folder() / filename
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(filepath, format="PNG")
    return filepath


def main():
    print("=== QR Code Generator Utility ===")
    data = input("Enter the data to encode in the QR code: ").strip()

    if not data:
        print("No data entered. Exiting.")
        return

    print(f"QR code saved to: {generate_qr(data)}")


if __name__ == "__main__":
    main()
