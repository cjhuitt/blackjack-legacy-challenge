#!/usr/bin/env python3

import db
from deck import Deck


class Player():
    def __init__(self, name, money):
        self.__cards = []
        self.__name = name
        self.__money = money
        self.__bet = 0

    def name(self):
        return self.__name

    def money(self):
        return self.__money

    def cards(self):
        return self.__cards

    def dealCard(self):
        card = Deck().draw()
        self.__cards.append(card)
        return card

    def wager(self, amount):
        if self.__money < amount:
            raise Exception("Not enough money for wager.")
        self.__money -= amount
        db.Db().set_money(self.__name, self.__money)
        self.__bet += amount

    def getWager(self):
        return self.__bet

    def loseWager(self):
        bet = self.__bet
        self.__bet = 0
        return bet

    def winWager(self, payout):
        self.__bet = 0
        self.__money += payout
        db.Db().set_money(self.__name, self.__money)

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
        db.Db().set_money(self.__name, self.__money)
        self.__bet *= 2
        self.hit()
        self.stay()
        return self.__cards[-1]

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
            elif card.value() > 10:
                score += 10
            else:
                score += card.value()
        while score > 21 and aces > 0:
            aces -= 1
            score -= 10
        return score
