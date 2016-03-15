import itertools
from lc_vector import LCVector
from ngram_reader import NgramReader


class LanguageClassifier(object):
    def __init__(self, languages, ngram_len, verbose=True):
        self.languages = languages
        self.ngram_len = ngram_len
        self.verbose = verbose

    def calculate_vectors(self):
        if self.verbose:
            print "Calculating vectors.."
        alphabet = ' abcdefghijklmnopqrstuvwxyz'
        self.index_ngrams = map(
            ''.join, itertools.product(alphabet, repeat=self.ngram_len)
        )
        for language, data in self.languages.iteritems():
            if self.verbose:
                print language
            self.languages[language]['vector'] = self.calculate_average_vector(
                self.ngram_len, self.index_ngrams, data['samples']
            )
            if self.verbose:
                print '\r Done.'
        if self.verbose:
            print "Finished.\n"

    def determine_language(self, input_data):
        lc_vector = self.calculate_vector(self.ngram_len, text=input_data)
        min_dist = 2
        language_name = ''
        for language, data in self.languages.iteritems():
            dist = lc_vector.cos_distance(self.languages[language]['vector'])
            if dist < min_dist:
                min_dist = dist
                language_name = language
        return language_name, min_dist

    @classmethod
    def calculate_vector(cls, ngram_len, path=None, text=None):
        ngram_reader = None
        if text:
            ngram_reader = NgramReader(text=text)
        else:
            ngram_reader = NgramReader()
            ngram_reader.read_file(path)
        ngram_reader.remove_special_chars()
        ngrams = ngram_reader.generate_ngrams(ngram_len)
        lc_vector = LCVector(ngrams=ngrams, ngram_len=ngram_len)
        lc_vector.calculate_vector()
        return lc_vector

    @classmethod
    def calculate_average_vector(cls, ngram_len, index_ngrams, paths):
        vector = LCVector(vector=([0] * len(index_ngrams)))
        for path in paths:
            vector = vector + cls.calculate_vector(ngram_len, path)
        return vector / len(paths)
