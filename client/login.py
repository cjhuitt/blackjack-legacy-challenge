#!/usr/bin/env python3

from comm import Comm
import tkinter as tk


class LoginDialog(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.attributes('-topmost', True)
        self.grab_set()

        inputs = tk.Frame(self)
        inputs.pack()

        tk.Label(inputs, text="Username").grid(row=0)
        tk.Label(inputs, text="Password").grid(row=1)

        self.username = tk.Entry(inputs)
        self.username.grid(row=0, column=1)
        self.username.focus_set()

        self.password = tk.Entry(inputs)
        self.password.grid(row=1, column=1)

        buttons = tk.Frame(self)
        buttons.pack()

        btn_ok = tk.Button(buttons, default=tk.ACTIVE)
        btn_ok['text'] = 'OK'
        btn_ok['command'] = self.onOk
        btn_ok.pack(side='left')

        btn_cancel = tk.Button(buttons)
        btn_cancel['text'] = 'Cancel'
        btn_cancel['command'] = self.onCancel
        btn_cancel.pack(side='left')

        self.bind("<Return>", self.onOk)
        self.bind("<Escape>", self.onCancel)

    def onOk(self, event=None):
        Comm().send('login {0} {1}'.format(
                self.username['text'], self.password['text']))
        # TODO: Wait for response, if authorized, then: self.destroy()
        #       Also, put the username and money somewhere for the main dialog
        #       to use.

    def onCancel(self, event=None):
        self.quit()

    # TODO: Handle [x] window button.
