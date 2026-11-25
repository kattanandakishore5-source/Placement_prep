"""Day 2: Word Frequency Counter.

Reads a text file, strips punctuation, normalizes case, counts occurrences
of each word, and displays the top 10 most frequent words in descending order.
"""

import os
import string
import sys


def count_word_frequency(filepath=None):
    """Read a text file and return a sorted list of (word, count) tuples."""
    if filepath is None:
        # Default to sample.txt in the same directory as this script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, "sample.txt")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        # Remove punctuation and normalize to lowercase
        text = text.translate(str.maketrans("", "", string.punctuation))
        text = text.lower()

        words = text.split()

        if not words:
            print("No words found in the file.")
            return

        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        sorted_words = sorted(
            frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print("===== WORD FREQUENCY COUNTER =====")
        print("Top 10 Most Frequent Words:\n")

        for i, (word, count) in enumerate(sorted_words[:10], start=1):
            print(f"{i}. {word}: {count}")

    except FileNotFoundError:
        print("File not found")


def main():
    """Main execution function."""
    target_file = sys.argv[1] if len(sys.argv) > 1 else None
    count_word_frequency(target_file)


if __name__ == "__main__":
    main()
