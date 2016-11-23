#!/usr/bin/env python3

import socket
import ssl
import tkinter as tk

class BlackjackDialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padx=9, pady=9)

        context = ssl.create_default_context()
        context.load_verify_locations('../certs/server.crt')
        # Hard-coded for localhost, because this is an exercise.
        connection = context.wrap_socket(
                socket.socket(socket.AF_INET),
                server_hostname='localhost')
        connection.connect(('localhost', 2121))
        # In real life, we'd check the cert against the server hostname.
        # TODO: Talk to stuff
        connection.write('asdfghjkl'.encode('utf-8'))

        self.pack(expand=True, fill=tk.BOTH)

        self.frameCards = tk.Frame(self, pady=9)
        self.frameCards.pack(side='top', expand=True, fill=tk.BOTH)

        self.labelDealer = tk.Label(self.frameCards)
        self.labelDealer['text'] = 'Dealer'
        self.labelDealer.pack(side='top')

        self.labelDealerCards = tk.Label(self.frameCards)
        self.labelDealerCards['text'] = '____'
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
        self.labelPlayerCards['text'] = '____'
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

    def onWager(self):
        # TODO
        print('Wager:', self.spinWager.get())

    def onHit(self):
        # TODO
        print('Hit')

    def onStay(self):
        # TODO
        print('Stay')
