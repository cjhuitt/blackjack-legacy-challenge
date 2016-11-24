#!/usr/bin/env python3

from comm import Comm
import dialog
import login
import sys
import tkinter as tk


def main(argv):
    c = Comm()

    root = tk.Tk()
    root.geometry('320x240')
    dlg = dialog.BlackjackDialog(master=root)
    login_dlg = login.LoginDialog(master=root)

    def handle_message(message):
        if message is None:
            root.quit()
        name, *params = message.split(' ')
        if name == 'auth':
            def and_then():
                # TODO: Put money somewhere for the main dialog to use.
                Comm().set_listener(dlg.handle_message)
                login_dlg.onAuth()
            root.after(1, and_then)
        elif name == 'auth_fail':
            pass
    Comm().set_listener(handle_message)

    root.mainloop()
    c.disconnect()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
