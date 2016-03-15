import pickle
import sys
import dill
from language_classifier import *

languages = {
    'Polish': {
    },
    'English': {
    },
    'German': {
    },
    'Italian': {
    },
    'Spanish': {
    },
    'Finnish': {
    },
}

if __name__ == '__main__':
    ngram_len = int(sys.argv[1])
    for language, d in languages.iteritems():
        with open('cache/{0}{1}.data'.format(language.lower(), ngram_len)) as f:
            languages[language]['vector'] = pickle.load(f)

    classifier = LanguageClassifier(languages, ngram_len)

    while True:
        print classifier.determine_language(raw_input('> '))
