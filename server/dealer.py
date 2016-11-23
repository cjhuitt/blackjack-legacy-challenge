#!/usr/bin/env python3

from player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__(0)

    def play(self):
        while(self.score() < 17):
            self.hit()

    def name(self):
        return 'dealer'
