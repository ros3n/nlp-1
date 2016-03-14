import re


class NgramReader(object):
    def read_file(self, path):
        with open(path) as f:
            self.text = f.read()

    def remove_special_chars(self):
        self.text = re.sub('[^a-zA-Z\s\n\t\r]+', '', self.text)
        self.text = re.sub('[\s\n\r\t]+', ' ', self.text)

    def generate_ngrams(self, n):
        self.ngrams =  zip(*[self.text[i:] for i in range(n)])
        return self.ngrams
