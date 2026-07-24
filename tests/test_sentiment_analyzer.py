"""Unit tests for the sentiment analyzer
(``Sentiment_analyzer_for_prototypes/sentiment_analyzer.py``)."""
import pytest

from conftest import load_module

sentiment = load_module(
    "Sentiment_analyzer_for_prototypes/sentiment_analyzer.py", "sentiment_analyzer"
)


@pytest.fixture
def analyzer():
    return sentiment.SentimentAnalyzer()


def test_clean_text_lowercases_strips_punctuation_and_short_words(analyzer):
    assert analyzer.clean_text("Hello, WORLD! is a go") == ["hello", "world"]


def test_analyze_positive(analyzer):
    label, score, pos, neg = analyzer.analyze_sentiment(
        "This is amazing and wonderful and great"
    )
    assert label == "positive"
    assert score > 5
    assert (pos, neg) == (3, 0)


def test_analyze_negative(analyzer):
    label, score, pos, neg = analyzer.analyze_sentiment(
        "This is terrible awful and horrible"
    )
    assert label == "negative"
    assert score < -5
    assert (pos, neg) == (0, 3)


def test_analyze_neutral_when_no_meaningful_words(analyzer):
    assert analyzer.analyze_sentiment("!!! a") == ("neutral", 0.0, 0, 0)


def test_get_word_frequency_orders_by_count_and_drops_stopwords(analyzer):
    freq = analyzer.get_word_frequency(
        "the apple apple banana orange orange orange", top_n=10
    )
    assert freq == [("orange", 3), ("apple", 2), ("banana", 1)]


def test_get_word_frequency_respects_top_n(analyzer):
    freq = analyzer.get_word_frequency("aaa bbb ccc ddd", top_n=2)
    assert len(freq) == 2


def test_generate_ascii_cloud_empty(analyzer):
    assert analyzer.generate_ascii_cloud([]) == "No words to display"


def test_generate_ascii_cloud_scales_by_frequency(analyzer):
    cloud = analyzer.generate_ascii_cloud([("apple", 3), ("banana", 1)])
    # The most frequent word gets the largest (bold, upper) rendering.
    assert "**APPLE**" in cloud
    assert "BANANA" in cloud
