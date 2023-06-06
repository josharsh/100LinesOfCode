import matplotlib.pyplot as plt
from collections import Counter


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def count_words(lyrics):
    words = lyrics.lower().split()
    word_freq = Counter(words)
    return word_freq


if __name__ == "__main__":
    lyrics = read_file("lyrics.txt")
    word_freq = count_words(lyrics)

    # Get 10 most common words
    common_words = word_freq.most_common(10)

    words = [item[0] for item in common_words]
    counts = [item[1] for item in common_words]

    plt.barh(words, counts, color='skyblue')
    plt.xlabel("Count")
    plt.ylabel("Word")
    plt.title("Top 10 Words")
    plt.show()
