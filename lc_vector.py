from collections import Counter, defaultdict
import itertools

class LCVector(object):
    def __init__(self, ngrams=None, ngram_len=None, vector=None):
        self.ngrams = ngrams
        self.counter = Counter(ngrams)
        self.ngram_len = ngram_len
        self.vector = vector or defaultdict(lambda: 0.0)

    def calculate_vector(self):
        n_factor = float(len(self.ngrams))
        for k in self.counter.keys():
            self.vector[k] = self.counter[k] / n_factor
        return self.vector

    def __add__(self, other):
        key_set = set()
        key_set.update(self.vector.keys())
        key_set.update(other.vector.keys())
        return LCVector(
            vector=defaultdict(
                lambda: 0.0,
                {k: self.vector[k] + other.vector[k] for k in key_set}
            ),
            ngram_len=self.ngram_len
        )

    def __div__(self, divider):
        return LCVector(
            vector=defaultdict(
                lambda: 0.0,
                {k: self.vector[k] / divider for k in self.vector.keys()}
            ),
            ngram_len=self.ngram_len
        )

    def cos_distance(self, other):
        key_set = set()
        key_set.update(self.vector.keys())
        key_set.update(other.vector.keys())
        numerator = sum([self.vector[k] * other.vector[k] for k in key_set])
        denominator = (27**(self.ngram_len))**2
        return 1 -  numerator / denominator
