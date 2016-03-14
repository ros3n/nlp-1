from collections import Counter
import itertools

class LCVector(object):
    def __init__(self, ngrams=None, ngram_len=None, vector=None):
        self.ngrams = ngrams
        self.counter = Counter(ngrams)
        self.ngram_len = ngram_len
        self.vector = vector

    def calculate_vector(self):
        alphabet = ' abcdefghijklmnopqrstuvwxyz'
        self.vector = [
            self.counter[k] for k in map(
                ''.join, itertools.product(alphabet, repeat=self.ngram_len)
            )
        ]
        return self.vector

    def __add__(self, other):
        return LCVector(
            vector=map(lambda x: x[0] + x[1], zip(self.vector, other.vector))
        )

    def __div__(self, divider):
        return LCVector(
            vector=map(lambda x: x / divider, self.vector)
        )
