"""Unit tests for the Morse translator (``morse_translator/morse_translator.py``)."""
import pytest

from conftest import load_module

morse = load_module("morse_translator/morse_translator.py", "morse_translator")


def test_encrypt_single_word():
    assert morse.encrypt("SOS") == "... --- ... "


def test_encrypt_digits():
    assert morse.encrypt("123") == ".---- ..--- ...-- "


def test_encrypt_uses_space_between_letters_and_double_space_between_words():
    assert morse.encrypt("HI THERE").startswith(".... ..  ")


@pytest.mark.parametrize("message", ["HELLO", "HELLO WORLD", "ABC XYZ"])
def test_encrypt_decrypt_roundtrip(message):
    assert morse.decrypt(morse.encrypt(message)) == message


def test_decrypt_known_value():
    assert morse.decrypt("... --- ...") == "SOS"


def test_encrypt_unknown_character_raises():
    with pytest.raises(KeyError):
        morse.encrypt("hello")  # lowercase is not in the code table
