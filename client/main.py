#!/usr/bin/env python3

import dialog
import sys
import tkinter as tk


def main(argv):
    root = tk.Tk()
    root.geometry('320x240')
    dlg = dialog.BlackjackDialog(master=root)
    dlg.mainloop()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
