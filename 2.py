import sys
from language_classifier import *

languages = {
    'Polish': {
        'samples': [
            'samples/polski.txt',
            'samples/polski2.txt',
            'samples/polski3.txt'
        ],
    },
    'English': {
        'samples': [
            'samples/Harry Potter 1 Sorcerer\'s_Stone.txt',
            'samples/Harry Potter 2 Chamber_of_Secrets.txt',
            'samples/Harry Potter 3 Prisoner of Azkaban.txt',
            'samples/Harry Potter 4 and the Goblet of Fire.txt',
        ],
    },
    'German': {
        'samples': [
            'samples/2momm10.txt',
            'samples/4momm10.txt',
            'samples/5momm10.txt',
            'samples/8momm10.txt',
        ],
    },
    'Italian': {
        'samples': ['samples/54.txt', 'samples/q.txt'],
    },
    'Spanish': {
        'samples': ['samples/spanish.txt', 'samples/spanish1.txt'],
    },
    'Finnish': {
        'samples': ['samples/finnish.txt', 'samples/finnish1.txt'],
    },
}

if __name__ == '__main__':

    classifier = LanguageClassifier(languages, int(sys.argv[1]))
    classifier.calculate_vectors()

    while True:
        print classifier.determine_language(raw_input('> '))
