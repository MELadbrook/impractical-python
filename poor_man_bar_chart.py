"""Create a simple bar chart to show number of each letter in a sentence."""

from pprint import pprint
from _collections import defaultdict

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def gather_letters():
    """Create a bar chart of letters from a input sentence."""
    while True:
        sentence = input("Type a sentence: \n")
        print("\n")
        letters = defaultdict(list)
        for letter in sentence:
            letter = letter.lower()
            if letter in ALPHABET:
                letters[letter].append(letter)
        pprint(letters, width=110)


if __name__ == "__main__":
    gather_letters()
