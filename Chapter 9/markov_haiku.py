import sys
import logging
import random
from collections import defaultdict
from count_syllables import count_syllables

logging.disable(logging.CRITICAL)  # comment out to enable debugging messages
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def load_training_file(file):
    """Return text file as a string."""
    with open(file) as f:
        raw_haiku = f.read()
        return raw_haiku


def prop_training(raw_haiku):
    """Load string, remove newline, split words on spaces, and return list."""
    corpus = raw_haiku.replace('\n', ' ').split()
    return corpus


def map_word_to_word(corpus):
    """Load list & use dictionary to map word to word that follows."""
    limit = len(corpus) - 1
    dict1_to_1 = defaultdict(list)
    for index, word in enumerate(corpus):
        if index < limit:
            suffix = corpus[index + 1]
            dict1_to_1[word].append(suffix)
    logging.debug("map_word_to_word results for \"sake\" = %s\n",
                  dict1_to_1['sake'])
    return dict1_to_1


def map_2_words_to_word(corpus):
    """Load list & use dictionary to map word-pair to trailing word."""
    limit = len(corpus) - 2
    dict2_to_1 = defaultdict(list)
    for index, word in enumerate(corpus):
        if index < limit:
            key = word + ' ' + corpus[index + 1]
            suffix = corpus[index + 2]
            dict2_to_1[key].append(suffix)
    logging.debug("map_2_words_to_word results for \"sake jug\" = %s\n",
                  dict2_to_1['sake jug'])
    return dict2_to_1


def random_word(corpus):
    """Return random word and syllable count from training corpus."""
    word = random.choice(corpus)
    num_syls = count_syllables(word)
    if num_syls > 4:
        random_word(corpus)
    else:
        logging.debug("random word & syllables = %s %s\n", word, num_syls)
        return (word, num_syls)