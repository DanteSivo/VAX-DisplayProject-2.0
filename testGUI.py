#!/usr/bin/env python3

# Display UTC.
# started with https://docs.python.org/3.4/library/tkinter.html#module-tkinter

import tkinter as tk
import time



def getCount():
    global globalX
    globalX *= 2
    return globalX + 1

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=('Helvetica', 24))
        self.time.pack(side="top")
        self.time["textvariable"] = self.now

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        # update displayed time
        self.now.set(getCount())
        # schedule timer to call myself after 1 second
        self.after(1000, self.onUpdate)

globalX = 1
window = tk.Tk()
window.title("GUI")
window.geometry("800x480")
window.config(bg = '#024889')

app = Application(master=window)
window.mainloop()