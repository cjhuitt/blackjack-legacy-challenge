#!/usr/bin/env python3

from dealer import Dealer
from deck import Deck
from player import Player
from singleton import Singleton


class Game(metaclass=Singleton):
    def __init__(self):
        self.__players = [Player(1000)] # TODO: Load player money from DB.
        self.__dealer = Dealer()

    # TODO: Accept wagers

    def deal(self):
        for _ in range(2):
            for player in self.__players:
                player.dealCard()
        self.__dealer.dealCard()
        self.__dealer.dealCard()

    # TODO: Get player actions

    def endHand(self):
        self.__dealer.play()

        if self.__dealer.score() > 21:
            for player in self.__players:
                if player.score() == 21 and len(player.cards()) == 2:
                    player.winWager(player.getWager() * 2.5)
                else:
                    player.winWager(player.getWager() * 2)
        elif self.__dealer.score() == 21 and len(self.__dealer.cards()) == 2:
            for player in self.__players:
                if player.score() == 21 and len(player.cards()) == 2:
                    player.winWager(player.getWager())
                else:
                    player.loseWager()
        else:
            for player in self.__players:
                if player.score() == 21 and len(player.cards()) == 2:
                    player.winWager(player.getWager() * 2.5)
                elif player.score() > self.__dealer.score():
                    player.winWager(player.getWager() * 2)
                elif player.score() == self.__dealer.score():
                    player.winWager(player.getWager())
                else:
                    player.loseWager()

        for player in self.__players:
            player.endHand()
        self.__dealer.endHand()
        Deck().shuffle()
