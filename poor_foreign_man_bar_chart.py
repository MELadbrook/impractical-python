"""Create a simple bar chart to show number of each letter in a sentence."""

from pprint import pprint
from _collections import defaultdict

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def gather_letters():
    """Create a bar chart of letters from a input sentence."""
    while True:
        sentence = input("Type a sentence: \n")
        print("\n")
        alph_dict = defaultdict(list)
        for i in ALPHABET:
            alph_dict[i].append('')
        for letter in sentence:
            if letter in ALPHABET:
                alph_dict[letter].extend(letter)
        pprint(alph_dict, width=110)


if __name__ == "__main__":
    gather_letters()
