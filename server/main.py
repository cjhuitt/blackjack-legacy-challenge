#!/usr/bin/env python3

from comm import Comm
from command_dispatcher import CommandDispatcher
from db import Db
from game import Game
import features
import sys


def handle_auth(params, game, db, comms):
    if len(params) != 2:
        comms.send('auth_fail')
        return
    if db.auth(*params):
        money = db.money(params[0])
        comms.send('auth {0}'.format(money))
        game.begin()
    else:
        comms.send('auth_fail')


def main(argv):
    c = Comm()
    g = Game()
    db = Db()

    def auth(params):
        nonlocal g
        nonlocal db
        nonlocal c
        handle_auth(params=params, game=g, db=db, comms=c)

    def feat(params):
        nonlocal c
        features.handle_features_request(comms=c)

    dispatcher = CommandDispatcher()
    dispatcher.add_command('login', auth)
    dispatcher.add_command('features', feat)

    while (True):
        c.wait()
        message = c.receive()
        if message is not None:
            name, *params = message.split(' ')
            dispatcher.dispatch_command(command=name, parameters=params)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
