#! -*- encoding: utf-8 -*-

import pickle
import sys
import dill
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
    sample_sentences = [
        'To jest przykladowy tekst. Zostanie wykorzystany do przeanalizowania dzialania klasyfikatora',
        'This is a sample sentence. It will be used for language classifier tests.',
        'Si tratta di una frase di esempio. Sarà usato per i test di lingua classificatore.',
        'Dies ist ein Beispielsatz. Es wird für den Sprach Klassifikator Tests verwendet werden.',
        'Esta es una sentencia de la muestra. Será utilizado para las pruebas de lenguaje clasificador.',
        'Tämä on näyte lause. Sitä käytetään kielen luokitin testejä.',
    ]

    for i in xrange(1, 11):
        for language, d in languages.iteritems():
            with open('cache/{0}{1}.data'.format(language.lower(), i)) as f:
                languages[language]['vector'] = pickle.load(f)
        classifier = LanguageClassifier(languages, i)

        for sentence in sample_sentences:
            print sentence
            print i, classifier.determine_language(sentence)
            print
