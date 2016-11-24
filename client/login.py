#!/usr/bin/env python3

from comm import Comm
from user import User
import tkinter as tk


class LoginDialog(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.__authorized = False

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
        self.bind("<Destroy>", self.onDestroy)

    def onAuth(self):
        self.__authorized = True
        self.destroy()

    def onOk(self, event=None):
        Comm().send('login {0} {1}'.format(
                self.username.get(), self.password.get()))
        User().name = self.username.get()

    def onCancel(self, event=None):
        self.quit()

    def onDestroy(self, event=None):
        if not self.__authorized:
            self.quit()
