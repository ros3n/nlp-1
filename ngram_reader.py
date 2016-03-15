import re


class NgramReader(object):
    def __init__(self, text=None):
        if text:
            self.text = text

    def read_file(self, path):
        with open(path) as f:
            self.text = f.read()

    def remove_special_chars(self):
        self.text = self.text.lower()
        self.text = re.sub('[^a-zA-Z\s\n\t\r]+', '', self.text)
        self.text = re.sub('[\s\n\r\t]+', ' ', self.text)

    def generate_ngrams(self, n):
        split_ngrams = zip(*[self.text[i:] for i in range(n)])
        self.ngrams = map(lambda x: ''.join(x), split_ngrams)
        return self.ngrams
