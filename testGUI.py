#!/usr/bin/env python3

# Display UTC.
# started with https://docs.python.org/3.4/library/tkinter.html#module-tkinter

from tkinter import *
import time



def getCount():
    global globalX
    globalX += 1
    return globalX

class Application(Frame):
    def __init__(self, master=None):
        self.frame = Frame.__init__(self, master, width = 800, height = 480)
        self.pack()

        self.createWidgets()

    def createWidgets(self):
        # To Be Deleted

        self.photo = PhotoImage(file="images\sprocket150.png")
        self.w = Label(window, image=self.photo, bg='#024889')
        self.w.photo = self.photo
        self.w.place(x=30, y=30)

        self.eventVar = StringVar()
        self.eventLabel = Label(self, font=("Tahoma", 26), fg='#fcd200', bg = '#024889')
        self.eventLabel.place(x=400, y=225, anchor="center")
        self.eventLabel["textvariable"] = self.eventVar

        self.timeVar = StringVar()
        self.timeLabel = Label(self, font=("Tahoma", 20), fg='#fcd200', bg = '#024889')
        self.timeLabel.place(x=400,y=275, anchor="center")
        self.timeLabel["textvariable"] = self.timeVar

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        # update displayed time
        var = getCount()
        self.eventVar.set(var)
        self.timeVar.set(var)
        # schedule timer to call myself after 1 second
        self.after(1000, self.onUpdate)

globalX = 1
window = Tk()
window.title("GUI")
window.geometry("800x480")
window.config(bg = '#024889')

app = Application(master=window)
window.mainloop()