#!/usr/bin/env python3

# Display UTC.
# started with https://docs.python.org/3.4/library/tkinter.html#module-tkinter

import tkinter as tk
import time



def getCount():
    global globalX
    globalX += 1
    return globalX

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # To Be Deleted
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=('Helvetica', 24))
        #self.time.pack(side="top")
        self.time["textvariable"] = self.now

        self.eventVar = tk.StringVar()
        self.eventLabel = tk.Label(self, font=("Tahoma", 26), fg='#fcd200', bg = '#024889')
        self.eventLabel.place(x=400, y=225, anchor="center")
        self.eventLabel.pack()
        self.eventLabel["textvariable"] = self.eventVar

        self.timeVar = tk.StringVar()
        self.eventLabel = tk.Label(self, font=("Tahoma", 20), fg='#fcd200', bg = '#024889')
        self.eventLabel.place(x=400,y=275, anchor="center")
        self.eventLabel.pack()
        self.eventLabel["textvariable"] = self.timeVar

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        # update displayed time
        var = getCount()
        self.now.set(var)
        self.eventVar.set(var)
        self.timeVar.set(var)
        # schedule timer to call myself after 1 second
        self.after(1000, self.onUpdate)

globalX = 1
window = tk.Tk()
window.title("GUI")
window.geometry("800x480")
window.config(bg = '#024889')

app = Application(master=window)
window.mainloop()