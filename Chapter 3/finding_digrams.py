import sys
from itertools import permutations
from collections import Counter
import load_dictionary

#user_name = input("Please enter a name: ")


def make_digrams(word):
    digrams = []
    count = 0
    for i in range(len(word)-1):
        print(i)
        digrams.append(word[count:count + 2])
        count += 1
    return digrams


print(make_digrams('ladbrook'))