import itertools
from collections import defaultdict

def char_counter(word):
    char_w = defaultdict(int)
    for char in word:
        char_w[char] += 1
    return char_w,word

def anagrammer_match(w1,w2):
    if w1[0].viewitems() == w2[0].viewitems():
        return "ANAGRAM found", w1[1],w2[1]
    else:
        return "NOT an ANAGRAM", w1[1],w2[1]

def anagrammer(words):
    char_count=[char_counter(word) for word in words]
    count_pairs=list(itertools.combinations(char_count,2))
    return [anagrammer_match(pair[0],pair[1]) for pair in count_pairs]
