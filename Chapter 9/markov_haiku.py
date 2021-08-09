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