#!/usr/bin/env python3

from player import Player
from singleton import Singleton
import sqlite3


class Db(metaclass=Singleton):
    def __init__(self):
        self.db = sqlite3.connect('blackjack.db')

    def players(self):
        c = self.db.cursor()
        players = []
        for name, money in c.execute('SELECT name,money FROM Players'):
            players.append(Player(name, money))
        return players

    def money(self, player):
        c = self.db.cursor()
        c.execute('SELECT money FROM Players WHERE name="' + player + '"')
        return int(c.fetchone()[0])

    def set_money(self, player, money):
        c = self.db.cursor()
        c.execute('UPDATE Players SET money=' + str(money) +
                  ' WHERE name="' + player + '"')
        self.db.commit()

    def auth(self, player, password):
        c = self.db.cursor()
        c.execute('SELECT * FROM Players WHERE name="' + player + '" ' +
                  ' AND password="' + password + '"')
        return c.fetchone() is not None

    def print(self):
        c = self.db.cursor()
        for name, password, money in c.execute('SELECT name,password,money FROM Players'):
            print('{} ({}): {}'.format(name, password, money))
