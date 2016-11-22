#!/usr/bin/env python3

from deck import Deck


class Player():
    def __init__(self, money):
        self.__cards = []
        self.__money = money
        self.__bet = 0

    def money(self):
        return self.__money

    def cards(self):
        return self.__cards

    def dealCard(self):
        self.__cards.append(Deck().draw())

    def wager(self, amount):
        if self.__money < amount:
            raise Exception("Not enough money for wager.")
        self.__money -= amount
        self.__bet += amount

    def loseWager(self):
        bet = self.__bet
        self.__bet = 0
        return bet

    def winWager(self, payout):
        self.__bet = 0
        self.__money += payout

    def hit(self):
        if self.score() >= 21:
            raise Exception("Can't hit with score over 20.")
        self.__cards.append(Deck().draw())

    def stay(self):
        pass

    def doubleDown(self):
        if self.__money < self.__bet:
            raise Exception("Not enough money to double down.")
        self.__money -= self.__bet
        self.__bet *= 2
        self.hit()
        self.stay()

    def split(self):
        # TODO
        pass

    def buyInsurance(self, amount):
        # TODO
        pass

    def endHand(self):
        Deck().discard(self.__cards)
        self.__cards = []

    def score(self):
        aces = 0
        score = 0
        for card in self.__cards:
            if card.value() == 1:
                aces += 1
                score += 11
            else:
                score += card.value()
        while score > 21 and aces > 0:
            aces -= 1
            score -= 10
        return score
