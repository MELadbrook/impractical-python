r"""Encrypt a Civol War 'rail fence' type cipher.

This is for a "2-rail" fence cipher for short messages.

Example text to encrypt: 'Buy more Maine potatoes'

Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S

Read zigzag:       \/\/\/\/\/\/\/\/\/\/

Encrypted:    BYOEA NPTTE UMRMI EOSOS

"""

#====================================================================
# USER INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """Let us cross over the river and rest under the shade of the
 trees"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#===================================================================


def main():
    """Run program to encrypt message using 2-rail fence cipher."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)