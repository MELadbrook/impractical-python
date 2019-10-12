"""Removes single letter words from a dictionary file."""

import load_dictionary

word_list = load_dictionary.load('palindromes_words.txt')
final_list = []


def remove_singles():
    """Remove single letter words."""
    for word in word_list:
        if len(word) > 1:
            final_list.append(word)
    return final_list


if __name__ == "__main__":
    remove_singles()
