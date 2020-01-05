from tkinter import *
import quickstart
import time

def updateEvent():
    eventsList = quickstart.main()
    if (len(eventsList) <= 0):
       return ["No events ongoing or planned!", ""]
    else: # There must be at least 1 event in the calendar
        startTime = eventsList[0]['start'].get('dateTime', eventsList[0]['start'].get('date')).split('T') # basic parsing
        startDate = startTime[0] # End date of the event
        startTime = startTime[1] # Start time of the Event
        endTime = eventsList[0]['end'].get('dateTime', eventsList[0]['start'].get('date')).split('T') # basic parsing
        endDate = endTime[0] # End date of the event
        endTime = endTime[1] # End time of the event

        return [startDate, startTime]
    return [eventsList, eventsList]

class Application(Frame):
    def __init__(self, master=None):
        self.frame = Frame.__init__(self, master, width = 800, height = 480, bg = '#024889')
        self.pack()

        self.createWidgets()

    def createWidgets(self):
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
        displayStr = updateEvent()
        self.eventVar.set(displayStr[0])
        self.timeVar.set(displayStr[1])
        self.after(250, self.onUpdate) # Loop update


window = Tk()
window.title("VAX Reservation Display")
window.geometry("800x480")
window.config(bg = '#024889')

app = Application(master=window)
window.mainloop()