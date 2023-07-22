#!/bin/python3

import math
import os
import random
import re
import sys


from collections import defaultdict
#
# Complete the 'getSearchResults' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY words
#  2. STRING_ARRAY queries
#

def buildAnagramGroups(words):
    anagramGroups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagramGroups[sorted_word].append(word)
    return anagramGroups

def getSearchResults(words, queries):
    anagramGroups = buildAnagramGroups(words)
    results = []

    for query in queries:
        sortedQuery = ''.join(sorted(query))
        if sortedQuery in anagramGroups:
            anagrams = sorted(anagramGroups[sortedQuery])
            results.append(anagrams)
        else:
            results.append([])

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    result = getSearchResults(words, queries)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
