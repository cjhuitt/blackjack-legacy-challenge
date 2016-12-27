#!/usr/bin/env python3

from comm import Comm
from db import Db
from game import Game
import sys


def main(argv):
    c = Comm()
    g = Game()
    while (True):
        c.wait()
        message = Comm().receive()
        if message is not None:
            name, *params = message.split(' ')
            if name == 'login':
                if Db().auth(*params):
                    money = Db().money(params[0])
                    Comm().send('auth {0}'.format(money))
                    g.begin()
                else:
                    Comm().send('auth_fail')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
