#!/usr/bin/env python3

from comm import Comm
import dialog
import sys
import tkinter as tk


def main(argv):
    c = Comm()
    root = tk.Tk()
    root.geometry('320x240')
    dlg = dialog.BlackjackDialog(master=root)
    dlg.mainloop()
    c.disconnect()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
