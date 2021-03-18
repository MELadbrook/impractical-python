import sys
import string


def load_text(file):
    """Load a text file as a string."""
    with open(file) as f:
        return f.read().strip()


def solve_null_cipher(message, lookahead):
    """Solve a null cipher based on number of letters after punctuation mark.

    message = null cipher as string stripped of whitespace
    lookahead = endpoint of range of letters after punctuation mark to
     examine"""
    for i in range(1, lookahead + 1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print("Using offset of {} after punctuation = {}".
              format(i, plaintext))
    print()