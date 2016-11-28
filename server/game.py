#!/usr/bin/env python3

from comm import Comm
from db import Db
from dealer import Dealer
from deck import Deck
from player import Player
from singleton import Singleton
import time


class Game(metaclass=Singleton):
    def __init__(self):
        self.__players = Db().players()
        self.__dealer = Dealer()

    def begin(self):
        while True:
            wagers = {}
            while len(wagers) < len(self.__players):
                message = Comm().receive()
                if message is None:
                    return
                w = message.split(' ')
                if w[0] == 'wager':
                    wagers[w[1]] = int(w[2])
            for name, amount in wagers.items():
                for player in self.__players:
                    if name == player.name():
                        player.wager(amount)
                        break

            self.deal()
            while True:
                message = Comm().receive()
                if message is None:
                    return
                name, *params = message.split(' ')
                if name == 'hit':
                    card = self.__players[0].dealCard()
                    Comm().send('deal {0} {1}'.format(
                            self.__players[0].name(), str(card)))
                if name == 'stay':
                    break
            card = self.__dealer.dealCard()
            Comm().send('deal {0} {1}'.format(self.__dealer.name(), str(card)))
            self.endHand()

    def deal(self):
        for _ in range(2):
            for player in self.__players:
                card = player.dealCard()
                Comm().send('deal {0} {1}'.format(player.name(), str(card)))
        card = self.__dealer.dealCard()
        Comm().send('deal {0} {1}'.format(self.__dealer.name(), str(card)))

    def endHand(self):
        self.__dealer.play()

        if self.__dealer.score() > 21:
            for player in self.__players:
                if player.score() == 21 and len(player.cards()) == 2:
                    amount = player.getWager() * 2.5
                    Comm().send('win {0} {1}'.format(player.name(), amount))
                    player.winWager(amount)
                elif player.score() > 21:
                    amount = player.getWager()
                    Comm().send('lose {0} {1}'.format(player.name(), amount))
                    player.loseWager()
                else:
                    amount = player.getWager() * 2
                    Comm().send('win {0} {1}'.format(player.name(), amount))
                    player.winWager(amount)
        elif self.__dealer.score() == 21 and len(self.__dealer.cards()) == 2:
            for player in self.__players:
                if player.score() == 21 and len(player.cards()) == 2:
                    Comm().send('push {0}'.format(player.name()))
                    player.winWager(player.getWager())
                else:
                    amount = player.getWager()
                    Comm().send('lose {0} {1}'.format(player.name(), amount))
                    player.loseWager()
        else:
            for player in self.__players:
                if player.score() == 21 and len(player.cards()) == 2:
                    amount = player.getWager() * 2.5
                    Comm().send('win {0} {1}'.format(player.name(), amount))
                    player.winWager(amount)
                elif player.score() > 21:
                    amount = player.getWager()
                    Comm().send('lose {0} {1}'.format(player.name(), amount))
                    player.loseWager()
                elif player.score() > self.__dealer.score():
                    amount = player.getWager() * 2
                    Comm().send('win {0} {1}'.format(player.name(), amount))
                    player.winWager(amount)
                elif player.score() == self.__dealer.score():
                    Comm().send('push {0}'.format(player.name()))
                    player.winWager(player.getWager())
                else:
                    amount = player.getWager()
                    Comm().send('lose {0} {1}'.format(player.name(), amount))
                    player.loseWager()

        for player in self.__players:
            player.endHand()
        self.__dealer.endHand()
        Deck().shuffle()
        time.sleep(5)
        Comm().send('reset')
