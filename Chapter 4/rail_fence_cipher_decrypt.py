r"""Encrypt a Civol War 'rail fence' type cipher.

This is for a "2-rail" fence cipher for short messages.

Example plaintext: 'Buy more Maine potatoes'

Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S

Read zigzag:       \/\/\/\/\/\/\/\/\/\/

Ciphertext:    BYOEA NPTTE UMRMI EOSOS

"""
import math
import itertools

#==================================================================
# USER INPUT:

# the string to be decrypted (paste between quotes):
ciphertext = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT
ES"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#=================================================================


