"""Unit tests for the password generator
(``password_generator/password_generator.py``)."""
import string

import pytest

from conftest import load_module

password_generator = load_module(
    "password_generator/password_generator.py", "password_generator"
)


@pytest.fixture
def generator():
    return password_generator.PasswordGenerator()


def test_respects_fixed_length_range(generator):
    for _ in range(50):
        pwd = generator.generate_random_password(
            min_length=12, max_length=12, lowercase=True
        )
        assert len(pwd) == 12


def test_length_within_bounds(generator):
    for _ in range(50):
        pwd = generator.generate_random_password(
            min_length=8, max_length=16, lowercase=True, digits=True
        )
        assert 8 <= len(pwd) <= 16


def test_lowercase_only_charset(generator):
    pwd = generator.generate_random_password(
        min_length=40, max_length=40, lowercase=True
    )
    assert all(c in string.ascii_lowercase for c in pwd)


def test_digits_only_charset(generator):
    pwd = generator.generate_random_password(
        min_length=40, max_length=40, digits=True
    )
    assert pwd.isdigit()


def test_uppercase_only_charset(generator):
    pwd = generator.generate_random_password(
        min_length=40, max_length=40, uppercase=True
    )
    assert all(c in string.ascii_uppercase for c in pwd)


def test_no_options_returns_error(generator):
    assert generator.generate_random_password() == "Error: No options selected"
