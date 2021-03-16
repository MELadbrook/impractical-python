"""Decrypt a path through a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top & read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for nagative key values read UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext
"""
import sys

#=======================================================================
# USER INPUT:

# the string to be decrypted (type or paste between the triple-quotes):
ciphertext = """16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"""

# number of columns in the transposition matrix:
COLS = 4

# number of rows in the transposition matrix:
ROWS = 5

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
key = """-1 2 -3 4"""

# END OF USER INPUT
#======================================================================

# split elements into words, not letters

cipherlist = list(ciphertext.split())

# initialise variables


translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

# turn key_int into list of integers:
key_int = [int(i) for i in key.split()]

# turn columns into items in list of lists:
for k in key_int:
    if k < 0: # reading bottom-to-top of column
        col_items = cipherlist[start:stop]
    elif k > 0: # reading top-to-bottom of column
        col_items = list(reversed(cipherlist[start:stop]))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print("\nciphertext = {}".format(ciphertext))
print("\ntranslation matrix = ", *translation_matrix, sep="\n")
print("\nkey length = {}".format(len(key_int)))

# loop through nested lists popping off last item to new list:
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '

print("\nplaintext = {}".format(plaintext))


def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher): # range excludes 1-column ciphers
        if len_cipher % 1 == 0:
            factors.append(i)
    print("\nLength of cipher = {}".format(len_cipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)


def key_to_int(key):
    """Turn key into list of integers & check validity."""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
        or 0 in key_int:
        print("\nError - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int


def main():
    """Run program and print decrypted plaintext."""
    print("\nCiphertext = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format((ROWS)))
    print("Trying key = {}".format(key))

    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print("Plaintext = {}".format(plaintext))

