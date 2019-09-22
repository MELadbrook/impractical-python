"""Takes a word and forms it's pig latin equivalent"""

def pigify(word):
    """Takes first letter of word, adds it to the end, and adds 'ay'."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] not in vowels:
        return word[1:] + word[0] + 'ay'
    return word + 'way'
