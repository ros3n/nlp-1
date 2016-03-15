import sys
from utils import *

if __name__ == '__main__':
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    ngram_len = int(sys.argv[1])
    index_ngrams = map(''.join, itertools.product(alphabet, repeat=ngram_len))
    vector = calculate_average_vector(ngram_len, index_ngrams, sys.argv[2:])
    print vector.vector
