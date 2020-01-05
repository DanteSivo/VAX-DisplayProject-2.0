from tkinter import *

def getCount():
    global globalX
    globalX += 1
    return globalX

class Application(Frame):
    def __init__(self, master=None):
        self.frame = Frame.__init__(self, master, width = 800, height = 480, bg = '#024889')
        self.pack()

        self.createWidgets()

    def createWidgets(self):
        # To Be Deleted

        self.photo = PhotoImage(file="images\sprocket150.png")
        self.w = Label(window, image=self.photo, bg='#024889')
        self.w.photo = self.photo
        self.w.place(x=30, y=30)

        self.vaxLabel = Label(self, font=("Tahoma", 26), fg='#fcd200', bg = '#024889', text = "What's going on in the VAX?")
        self.vaxLabel.place(x=410, y=150, anchor="center")

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
        # Updates the display
        var = getCount()
        self.eventVar.set(var)
        self.timeVar.set(var)
        self.after(1000, self.onUpdate)

globalX = 1
window = Tk()
window.title("GUI")
window.geometry("800x480")
window.config(bg = '#024889')

app = Application(master=window)
window.mainloop()