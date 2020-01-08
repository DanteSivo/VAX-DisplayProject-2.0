from tkinter import *
import quickstart
from datetime import datetime

def updateEvent():
    eventsList = quickstart.main()
    if (len(eventsList) <= 0):
       return ["No events ongoing or planned!", ""]
   # There must be at least 1 event in the calendar
    start = eventsList[0]['start'].get('dateTime', eventsList[0]['start'].get('date')).split('T') # basic parsing
    startDate = start[0].split('-') # Start date of the event Y/M/D format
    startTime = start[1].split(':') # H/M/timeZone/S format
    end = eventsList[0]['end'].get('dateTime', eventsList[0]['start'].get('date')).split('T') # basic parsing
    endDate = end[0].split('-') # End date of the event Y/M/D format
    endTime = end[1].split('-') # End time of the event
    endTime = endTime[0].split(':') # H/M/S format
    eventOngoing = isEventOngoing(startTime, startDate, endTime, endDate)

    getTimeDisplay = timeParse(startTime, endTime)

    if (eventOngoing):
        # Update label text to show the event in ongoing
        return ["Right Now: " + eventsList[0].get('summary'), getTimeDisplay]
    return [eventsList, eventsList]

'''isEventOngoing() - A function that determines if an event is going on (TRUE) or if it's coming up (FALSE)
Parameters - Self descriptive, all passed in from updateEvent()
Output - FALSE = Event is not ongoing, TRUE = Event is ongoing
'''
def isEventOngoing(startTime, startDate, endTime, endDate):
    now = datetime.now() # %H - Hour, #M - Minute , %S - Second, %D - Date, %m - Month /%d - Day /%Y - Year using .strftime()
    if ((now.strftime('%Y') >= startDate[0]) & (now.strftime('%m') >= startDate[1]) & (now.strftime('%d') >= startDate[2])): # Check the date, if start was before or at current
        if ((now.strftime('%H') >= startTime[0]) & (now.strftime('%M') >= startTime[1]) & (now.strftime('%S') >= startTime[3])):
            return True
    return False # All other cases, event has been proven to not be ongoing

'''timeParse() - A function that returns the string to display about how long the event is on for.
'''
def timeParse(startTime, endTime):
    startHour = startTime[0:1]
    startHour = int(''.join(startHour))
    if (startHour > 12): # Determine if the Start Time is AM or PM
        startM = " PM"
        startHour -= 12
    else:
        startM = " AM"

    endHour = endTime[0:1]
    endHour = int(''.join(endHour))
    if (endHour > 12): # Determine if the End Time is AM or PM
        endM = " PM"
        endHour -= 12
    else:
        endM = " AM"
    return str(startHour) + ':' + startTime[1] + startM  + " - " + str(endHour) + ':' + endTime[1] + endM

class Application(Frame):
    def __init__(self, master=None): # Class constructor
        self.frame = Frame.__init__(self, master, width = 800, height = 480, bg = '#024889')
        self.pack()

        self.createWidgets()

    def createWidgets(self):
        self.photo = PhotoImage(file="images\sprocket150.png")
        self.w = Label(window, image=self.photo, bg='#024889')
        self.w.photo = self.photo
        self.w.place(x=20, y=20)

        self.vaxLabel = Label(self, font=("Tahoma", 26), fg='#fcd200', bg = '#024889', text = "What's going on in the VAX?")
        self.vaxLabel.place(x=410, y=150, anchor="center")

        self.eventVar = StringVar()
        self.eventLabel = Label(self, font=("Tahoma", 26), fg='#fcd200', bg = '#024889')
        self.eventLabel.place(x=400, y=250, anchor="center")
        self.eventLabel["textvariable"] = self.eventVar

        self.timeVar = StringVar()
        self.timeLabel = Label(self, font=("Tahoma", 20), fg='#fcd200', bg = '#024889')
        self.timeLabel.place(x=400,y=300, anchor="center")
        self.timeLabel["textvariable"] = self.timeVar

        self.clockVar = StringVar()
        self.clockLabel = Label(self, font=("Tahoma", 14), fg='#fcd200', bg='#024889')
        self.clockLabel.place(x=700, y=460, anchor="center")
        self.clockLabel["textvariable"] = self.clockVar

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        # Updates the display
        displayStr = updateEvent()
        self.eventVar.set(displayStr[0])
        self.timeVar.set(displayStr[1])
        now = datetime.now()
        self.clockVar.set(now.strftime("%H:%M:%S %m/%d/%Y"))
        self.after(250, self.onUpdate) # Loop update


window = Tk()
window.title("VAX Reservation Display")
window.geometry("800x480")
window.config(bg = '#024889')

app = Application(master=window)
window.mainloop()