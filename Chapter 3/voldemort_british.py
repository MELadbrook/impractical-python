"""British Brute force code for anagrams."""

import sys
from itertools import permutations
from collections import Counter
import load_dictionary

def main():
    """Load files, run filters, allow user to view anagrams by 1st letter."""
    name = 'tmvoordle'
    name = name.lower()

    word_list_ini = load_dictionary.load('palindromes_words.txt')
    trigrams_filtered = load_dictionary.load('least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)

def prep_words(name, word_list_ini):
    """Prep word list for finding anagrams."""
    print("length initial word_list = {}".format(len(word_list_ini)))
    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini
                 if len(word) == len_name]
    print("length of new word_list = {}".format(len(word_list)))
    return word_list
