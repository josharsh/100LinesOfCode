"""Unit tests for the Scytale Cipher project (``Scytale Cipher/cipher.py``)."""
import pytest

from conftest import load_module

cipher = load_module("Scytale Cipher/cipher.py", "scytale_cipher")


@pytest.mark.parametrize(
    "key, plaintext, expected",
    [
        (2, "HELLOWORLD", "HLOOLELWRD"),
        (5, "HELLOWORLD", "HWEOLRLLOD"),
    ],
)
def test_encrypt_known_values(key, plaintext, expected):
    assert cipher.encrypt(key, plaintext) == expected


@pytest.mark.parametrize("key", [2, 4, 5])
def test_encrypt_decrypt_roundtrip(key):
    # Round-trip is exact only when the length is a multiple of the key,
    # because encryption drops any trailing partial row.
    plaintext = "ABCDEFGHIJKLMNOPQRST"  # length 20
    assert len(plaintext) % key == 0
    ciphertext = cipher.encrypt(key, plaintext)
    assert cipher.decrypt(key, ciphertext) == plaintext


def test_encrypt_key_one_is_identity():
    assert cipher.encrypt(1, "TRANSPOSE") == "TRANSPOSE"


def test_encrypt_drops_incomplete_trailing_row():
    # "ABCDE" with key 2 forms rows [A,B],[C,D]; the trailing "E" is dropped.
    assert cipher.encrypt(2, "ABCDE") == "ACBD"


def test_encrypt_empty_string():
    assert cipher.encrypt(3, "") == ""
