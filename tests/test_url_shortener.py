"""Unit tests for the URL shortener (``url_shortener/url_shortener.py``)."""
import hashlib

import pytest

from conftest import load_module

url_shortener = load_module("url_shortener/url_shortener.py", "url_shortener")


@pytest.fixture
def shortener():
    return url_shortener.URLShortener()


def test_generate_short_url_matches_md5_prefix(shortener):
    long_url = "https://www.example.com/this/is/a/long/url"
    expected = hashlib.md5(long_url.encode()).hexdigest()[:8]
    assert shortener.generate_short_url(long_url) == expected


def test_short_url_length_is_eight(shortener):
    assert len(shortener.generate_short_url("https://python.org")) == 8


def test_shorten_url_is_deterministic(shortener):
    url = "https://cognition.ai"
    assert shortener.shorten_url(url) == shortener.shorten_url(url)


def test_shorten_then_expand_roundtrip(shortener):
    url = "https://github.com/josharsh/100LinesOfCode"
    short = shortener.shorten_url(url)
    assert shortener.expand_url(short) == url


def test_shorten_caches_mapping(shortener):
    url = "https://example.org"
    shortener.shorten_url(url)
    assert url in shortener.url_map


def test_expand_unknown_short_url(shortener):
    assert shortener.expand_url("deadbeef") == "Short URL not found"


def test_different_urls_produce_different_short_urls(shortener):
    a = shortener.shorten_url("https://a.example")
    b = shortener.shorten_url("https://b.example")
    assert a != b
