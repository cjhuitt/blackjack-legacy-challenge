#!/usr/bin/env python3

from comm import Comm
from threading import Lock
import queue
import tkinter as tk

class BlackjackDialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padx=9, pady=9)

        self.pack(expand=True, fill=tk.BOTH)

        self.frameCards = tk.Frame(self, pady=9)
        self.frameCards.pack(side='top', expand=True, fill=tk.BOTH)

        self.labelDealer = tk.Label(self.frameCards)
        self.labelDealer['text'] = 'Dealer'
        self.labelDealer.pack(side='top')

        self.labelDealerCards = tk.Label(self.frameCards)
        self.labelDealerCards['text'] = ''
        self.labelDealerCards.pack(side='top')

        self.frameWager = tk.Frame(self.frameCards)
        self.frameWager.pack(expand=True)

        self.labelWager = tk.Label(self.frameWager)
        self.labelWager['text'] = 'Wager ($):'
        self.labelWager.pack(side='left')

        self.spinWager = tk.Spinbox(self.frameWager, from_=0, to=999)
        self.spinWager.pack(side='left')

        self.buttonWager = tk.Button(self.frameWager)
        self.buttonWager['text'] = 'Done'
        self.buttonWager['command'] = self.onWager
        self.buttonWager.pack(side='left')

        self.labelPlayerCards = tk.Label(self.frameCards)
        self.labelPlayerCards['text'] = ''
        self.labelPlayerCards.pack(side='bottom')

        self.labelPlayer = tk.Label(self.frameCards)
        self.labelPlayer['text'] = 'Player'
        self.labelPlayer.pack(side='bottom')

        self.frameCommands = tk.Frame(self)
        self.frameCommands.pack(side='bottom')

        self.buttonHit = tk.Button(self.frameCommands)
        self.buttonHit['text'] = 'Hit Me'
        self.buttonHit['command'] = self.onHit
        self.buttonHit['state'] = tk.DISABLED
        self.buttonHit.pack(side='left')

        self.buttonStay = tk.Button(self.frameCommands)
        self.buttonStay['text'] = 'Stay'
        self.buttonStay['command'] = self.onStay
        self.buttonStay['state'] = tk.DISABLED
        self.buttonStay.pack(side='left')

        self.lock = Lock()
        self.messages = queue.Queue()
        self.after(100, self.process_messages)

    def process_messages(self):
        while True:
            try:
                with self.lock:
                    message = self.messages.get(block=False)
                name, *params = message.split(' ')
                if name == 'deal':
                    self.onDeal(*params)
                elif name == 'win':
                    pass
                elif name == 'push':
                    pass
                elif name == 'lose':
                    pass
                elif name == 'reset':
                    self.onReset(*params)
            except queue.Empty:
                break
        self.after(100, self.process_messages)

    def onReset(self):
        self.labelDealerCards['text'] = ''
        self.labelPlayerCards['text'] = ''
        # TODO: More

    def onDeal(self, player, card):
        if player == 'dealer':
            self.labelDealerCards['text'] += card + ' '
        # TODO: Update player cards.

    def handle_message(self, message):
        with self.lock:
            self.messages.put(message)

    def onWager(self):
        Comm().send('wager {0} {1}'.format('player', self.spinWager.get()))
        # TODO: Update UI state?

    def onHit(self):
        Comm().send('hit {0}'.format('player'))
        # TODO: Update UI state?

    def onStay(self):
        Comm().send('stay {0}'.format('player'))
        # TODO: Update UI state?
