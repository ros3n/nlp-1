import itertools
from lc_vector import LCVector
from ngram_reader import NgramReader


def calculate_vector(ngram_len, path):
    ngram_reader = NgramReader()
    ngram_reader.read_file(path)
    ngram_reader.remove_special_chars()
    ngrams = ngram_reader.generate_ngrams(ngram_len)
    lc_vector = LCVector(ngrams=ngrams, ngram_len=ngram_len)
    lc_vector.calculate_vector()
    return lc_vector


def calculate_average_vector(ngram_len, index_ngrams, paths):
    vector = LCVector(vector=([0] * len(index_ngrams)))
    for path in paths:
        vector = vector + calculate_vector(ngram_len, path)
    return vector / len(paths)
