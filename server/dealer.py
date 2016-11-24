#!/usr/bin/env python3

from comm import Comm
from player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__('dealer', 0)

    def play(self):
        while(self.score() < 17):
            self.hit()
            Comm().send('deal {0} {1}'.format(self.name(), str(self.cards()[-1])))
        self.stay()
