"""Recursively determines if a word is palindromic."""


def palindrome_recursive(word):
    """Inputs a word and decides if it is palindromic."""
    label = word
    while len(word) > 0:
        first = word[0]
        last = word[len(word)-1]
        if first != last:
            return "{} is not palindromic.".format(label)
        word = word[1:len(word)-1]
    return "{} is palindromic.".format(label)


print(palindrome_recursive("rotorrotorm"))
