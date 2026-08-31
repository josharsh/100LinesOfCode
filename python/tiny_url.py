"""Tiny URL - Minimal URL shortener using base62 encoding."""

import hashlib
import string

ALPHABET = string.ascii_letters + string.digits
BASE = len(ALPHABET)


def encode_url(url: str) -> str:
    """Shorten a URL to a compact string."""
    hash_val = int(hashlib.md5(url.encode()).hexdigest()[:8], 16)
    short = []
    while hash_val > 0:
        short.append(ALPHABET[hash_val % BASE])
        hash_val //= BASE
    return "".join(short[:6])


def decode_url(short: str) -> str:
    """Decode is not reversible with hashing - use lookup dict instead."""
    raise NotImplementedError("Use a database for reverse lookup")


if __name__ == "__main__":
    url = "https://github.com/josharsh/100LinesOfCode"
    short = encode_url(url)
    print(f"Original: {url}")
    print(f"Short:    {short}")
