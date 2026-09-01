"""Word frequency counter in under 100 lines."""


def word_freq(text: str) -> dict[str, int]:
    """Count word frequency in text."""
    words = text.lower().split()
    freq = {}
    for word in words:
        word = word.strip(".,!?;:\"'")
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: -x[1]))


if __name__ == "__main__":
    sample = "the cat sat on the mat the cat ate the rat"
    for word, count in word_freq(sample).items():
        print(f"{word}: {count}")
