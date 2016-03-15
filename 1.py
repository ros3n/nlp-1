import sys
from language_classifier import *


if __name__ == '__main__':
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    ngram_len = int(sys.argv[1])
    vector = LanguageClassifier.calculate_average_vector(ngram_len, sys.argv[2:])
    print vector.vector
