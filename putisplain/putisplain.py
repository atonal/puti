#!/usr/bin/env python3

import random
from enum import Enum, auto

class Sijamuoto(Enum):
    YKS_NOMINATIIVI = auto()  # opiskelija
    YKS_GENETIIVI = auto()  # opiskelijan
    YKS_ILLATIIVI = auto()  # opiskelijaan
    MON_NOMINATIIVI = auto()  # opiskelijat
    YKS_ADJEKTIIVI = auto()  # opiskeleva
    MON_ADJEKTIIVI = auto()  # opiskelevat
    MON_GENETIIVI = auto()  # opiskelijoiden

NEXT_STATES = {
        Sijamuoto.YKS_NOMINATIIVI: [
            Sijamuoto.YKS_NOMINATIIVI,
            Sijamuoto.YKS_ILLATIIVI,
            Sijamuoto.MON_NOMINATIIVI
            ],
        Sijamuoto.YKS_GENETIIVI: [
            Sijamuoto.YKS_NOMINATIIVI,
            Sijamuoto.YKS_ADJEKTIIVI,
            Sijamuoto.MON_ADJEKTIIVI,
            Sijamuoto.MON_NOMINATIIVI
            ],
        Sijamuoto.YKS_ILLATIIVI: [
            Sijamuoto.MON_NOMINATIIVI
            ],
        Sijamuoto.MON_NOMINATIIVI: [
            Sijamuoto.YKS_ILLATIIVI,
            Sijamuoto.MON_ADJEKTIIVI,
            Sijamuoto.MON_GENETIIVI
            ],
        Sijamuoto.YKS_ADJEKTIIVI: [
            Sijamuoto.YKS_NOMINATIIVI,
            Sijamuoto.YKS_ADJEKTIIVI
            ],
        Sijamuoto.MON_ADJEKTIIVI: [
            Sijamuoto.YKS_ILLATIIVI,
            Sijamuoto.MON_NOMINATIIVI,
            Sijamuoto.MON_ADJEKTIIVI
            ],
        Sijamuoto.MON_GENETIIVI: [
            Sijamuoto.MON_NOMINATIIVI
            ]
        }

WORDS = [
        {'p': 'Pussin', 't': 'Tissin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pussien', 't': 'Tissien', 'sijamuoto': Sijamuoto.MON_GENETIIVI},
        {'p': 'Puristajat', 't':'Tiristäjät', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Puntin', 't':'Tintin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Punttien', 't':'Tinttien', 'sijamuoto': Sijamuoto.MON_GENETIIVI},
        {'p': 'Puheet', 't':'Tiheet', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Puskiin', 't':'Tiskiin', 'sijamuoto': Sijamuoto.YKS_ILLATIIVI},
        {'p': 'Puhkuva', 't':'Tihkuva', 'sijamuoto': Sijamuoto.YKS_ADJEKTIIVI},
        {'p': 'Punainen', 't':'Tinainen', 'sijamuoto': Sijamuoto.YKS_ADJEKTIIVI},
        {'p': 'Puhkuvat', 't':'Tihkuvat', 'sijamuoto': Sijamuoto.MON_ADJEKTIIVI},
        {'p': 'Pupu', 't':'Tipu', 'sijamuoto': Sijamuoto.YKS_NOMINATIIVI},
        {'p': 'Pupun', 't':'Tipun', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Puun', 't':'Tiin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pusu', 't':'Tisu', 'sijamuoto': Sijamuoto.YKS_NOMINATIIVI},
        {'p': 'Pusun', 't':'Tisun', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pusut', 't':'Tisut', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Puput', 't':'Tiput', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Pupun', 't':'Tipun', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pulan', 't':'Tilan', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pulin', 't':'Tilin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pultti', 't':'Tiltti', 'sijamuoto': Sijamuoto.YKS_NOMINATIIVI},
        {'p': 'Pultin', 't':'Tiltin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pulttaajat', 't':'Tilttaajat', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Pulkka', 't':'Tilkka', 'sijamuoto': Sijamuoto.YKS_NOMINATIIVI},
        {'p': 'Pulkan', 't':'Tilkan', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pulkat', 't':'Tilkat', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Puulin', 't':'Tiilin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pummi', 't':'Timmi', 'sijamuoto': Sijamuoto.YKS_NOMINATIIVI},
        {'p': 'Pummin', 't':'Timmin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pummit', 't':'Timmit', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Pummaajat', 't':'Timmaajat', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Punttaajat', 't':'Tinttaajat', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Punttaava', 't':'Tinttaava', 'sijamuoto': Sijamuoto.YKS_ADJEKTIIVI},
        {'p': 'Punttaavat', 't':'Tinttaavat', 'sijamuoto': Sijamuoto.MON_ADJEKTIIVI},
        {'p': 'Puntti', 't':'Tintti', 'sijamuoto': Sijamuoto.YKS_NOMINATIIVI},
        {'p': 'Puntin', 't':'Tintin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Puntit', 't':'Tintit', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Pukki', 't':'Tikki', 'sijamuoto': Sijamuoto.YKS_NOMINATIIVI},
        {'p': 'Pukin', 't':'Tikin', 'sijamuoto': Sijamuoto.YKS_GENETIIVI},
        {'p': 'Pukit', 't':'Tikit', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI},
        {'p': 'Pukkaaja', 't':'Tikkaaja', 'sijamuoto': Sijamuoto.YKS_NOMINATIIVI},
        {'p': 'Pukkaajat', 't':'Tikkaajat', 'sijamuoto': Sijamuoto.MON_NOMINATIIVI}
        ]

def generate_name():
    first_word = random.choice(WORDS)
    second_word = random.choice(WORDS)
    while (first_word == second_word or second_word['sijamuoto'] not in NEXT_STATES[first_word['sijamuoto']]):
        second_word = random.choice(WORDS)

    return '{} {}'.format(first_word['p'], second_word['t'])

if __name__ == '__main__':
    name = generate_name()
    print(name)
