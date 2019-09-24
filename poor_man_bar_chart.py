"""Create a simple bar chart to show number of each letter in a sentence."""

from _collections import defaultdict


def gather_letters():
    """Create a bar chart of letters from a input setence."""
    while True:
        sentence = input("Type a sentence: \n")
        print("\n")
        d = defaultdict(int)
        for letter in sentence:
            d[letter] += 1
        d.items()


if __name__ == "__main__":
    gather_letters()

