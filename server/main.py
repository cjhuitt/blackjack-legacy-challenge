#!/usr/bin/env python3

from comm import Comm
from db import Db
from game import Game
import sys


def handle_auth(command, params, game, db, comms):
    if command == 'login':
        if db.auth(*params):
            money = db.money(params[0])
            comms.send('auth {0}'.format(money))
            game.begin()
        else:
            comms.send('auth_fail')


def main(argv):
    c = Comm()
    g = Game()
    while (True):
        c.wait()
        message = c.receive()
        if message is not None:
            name, *params = message.split(' ')
            handle_auth(command=name, params=params, game=g, db=Db(), comms=c)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
