"""Create a simple bar chart to show number of each letter in a sentence."""

from _collections import defaultdict
from pprint import pprint


def gather_letters():
    """Create a bar chart of letters from a input sentence."""
    while True:
        sentence = input("Type a sentence: \n")
        print("\n")
        letters = defaultdict(int)
        for letter in sentence:
            letters[letter] += 1
        pprint(letters, width=1)


if __name__ == "__main__":
    gather_letters()

