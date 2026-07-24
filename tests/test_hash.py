"""Unit tests for the file hashing utility (``Hash/hashing.py``)."""
import hashlib

import pytest

from conftest import load_module

hashing = load_module("Hash/hashing.py", "hashing")

CONTENT = b"hello world"


@pytest.fixture
def sample_file(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_bytes(CONTENT)
    return str(path)


@pytest.mark.parametrize("algorithm", ["md5", "sha1", "sha256", "sha512"])
def test_calculate_hash_matches_hashlib(sample_file, algorithm):
    expected = hashlib.new(algorithm, CONTENT).hexdigest()
    assert hashing.calculate_hash(sample_file, algorithm) == expected


def test_calculate_hash_empty_file(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_bytes(b"")
    assert hashing.calculate_hash(str(path), "sha256") == hashlib.sha256(b"").hexdigest()


def test_calculate_hash_reads_large_file_in_chunks(tmp_path):
    # Larger than the 8192-byte read buffer to exercise the chunked loop.
    data = b"x" * 20000
    path = tmp_path / "big.bin"
    path.write_bytes(data)
    assert hashing.calculate_hash(str(path), "md5") == hashlib.md5(data).hexdigest()


def test_calculate_hash_missing_file_exits(sample_file):
    with pytest.raises(SystemExit):
        hashing.calculate_hash("/no/such/file/exists.txt", "md5")
