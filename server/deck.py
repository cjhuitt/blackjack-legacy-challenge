#!/usr/bin/env python3

from random import shuffle
from singleton import Singleton


class Deck(metaclass=Singleton):
    class __Card():
        def __init__(self, deck, value, suit):
            self.__deck = deck
            self.__value = value
            self.__suit = suit

        def __str__(self):
            suits = {
                'hearts': '♥',
                'clubs': '♣',
                'diamonds': '♦',
                'spades': '♠'
            }
            values = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
            return values[self.__value] + suits[self.__suit]

        def value(self):
            return self.__value

        def suit(self):
            return self.__suit

    def __init__(self):
        self.__discarded = []
        self.__cards = []
        for value in range(1, 14):
            for suit in ['hearts', 'clubs', 'diamonds', 'spades']:
                self.__cards.append(Deck.__Card(self, value, suit))
        self.shuffle()

    def draw(self):
        return self.__cards.pop()

    def shuffle(self):
        self.__cards.extend(self.__discarded)
        self.__discarded = []
        shuffle(self.__cards)

    def discard(self, cards):
        self.__discarded.extend(cards)
