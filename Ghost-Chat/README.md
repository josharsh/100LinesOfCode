# GhostChat: Secure Encrypted Utility

A lightweight, terminal-based encryption/decryption tool designed for secure communication between friends using a shared secret key.

## Description

GhostChat allows you to send and receive secret messages without them being readable by anyone who doesn't have your shared key. It uses a character-shifting algorithm (Vigenère-inspired) within the printable ASCII range to turn your text into "ghostly" symbols and back again.

## Features

- **Shared Key Encryption**: Both parties use the same secret key for consistent results.
- **Bi-directional Chat**: Easily decrypt incoming messages and encrypt your replies in one session.
- **Symbolic Output**: Encrypted messages look like a mix of characters and symbols, making them perfect for copy-pasting into chat apps.
- **Concise**: Built in less than 40 lines of Python code!

## Installation

No external libraries are required. GhostChat runs purely on standard Python.

1. Ensure you have Python installed.
2. Download `ghost-chat.py`.

## Usage

1. Run the script:
   ```bash
   python ghost-chat.py
   # OR
   py ghost-chat.py
   ```
2. Enter your **Shared Secret Key** (ensure your friend uses the exact same key).
3. Paste an encrypted message into `sender(encrypt)` to see the decrypted version.
4. Type your message into `me(decrypt)` to get an encrypted string you can send back.

## Technologies Used

- **Language**: Python 3
- **Libraries**: `os` (standard library)
- **Algorithm**: Custom character-shifting via ASCII manipulation.

---

Part of the [100 Lines of Code](https://github.com/josharsh/100LinesOfCode) project.
