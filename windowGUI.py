from tkinter import *
import quickstart
from datetime import datetime

def updateEvent():
    eventsList = quickstart.main()
    if (len(eventsList) <= 0):
       return ["No events ongoing or planned!", ""]
   # There must be at least 1 event in the calendar

    event = vaxCheck(eventsList) # Are any of these events going on in the VAX???
    if (event == None):
        return ["No events planned", ""]

    start = event['start'].get('dateTime', event['start'].get('date')).split('T') # basic parsing
    startDate = start[0].split('-') # Start date of the event Y/M/D format
    startTime = start[1].split(':') # H/M/timeZone/S format
    end = event['end'].get('dateTime', event['start'].get('date')).split('T') # basic parsing
    endDate = end[0].split('-') # End date of the event Y/M/D format
    endTime = end[1].split('-') # End time of the event
    endTime = endTime[0].split(':') # H/M/S format
    eventOngoing = isEventOngoing(startTime, startDate, endTime, endDate)

    getTimeDisplay = timeParse(startTime, endTime)
    getEventDisplay = eventParse(eventsList[0].get('summary'))

    if (eventOngoing):
        # Update label text to show the event in ongoing
        return ["Right Now: " + getEventDisplay, getTimeDisplay]
    # if the event is in the future
    return ["Next Event: " + getEventDisplay, getTimeDisplay + ' ' + endDate[1] + '/' + endDate[2] + '/' + endDate[0]]

"""vaxCheck() - Determine the soonest event if any, that is in the VAX! Returns the event if found
"""
def vaxCheck(eventList):

    for index in range(len(eventList)):
        summary = eventList[index].get('summary')
        if ((summary.find("VAX") >= 0) or (summary.find("vax") >= 0) or (summary.find("Vax") >= 0)): # If the word VAX is in the title
            return eventList[index]
        location = eventList[index].get('location')
        if ((location.find("VAX") >= 0) or (location.find("vax") >= 0) or (location.find("Vax") >= 0)):
            return eventList[index]
    return None # If no event found within the range - return such

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

def eventParse(eventName):
    if (len(eventName) >= 35):
        if (eventName[34] != ' ' and eventName[35] != ' '):
            dash = '-'
        else:
            dash = ''
        eventName = eventName[0:35] + dash + '\n' + eventName[35:]
    return eventName

class Application(Frame):
    def __init__(self, master=None): # Class constructor
        self.frame = Frame.__init__(self, master, width = 800, height = 480, bg = '#024889')
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.photo = PhotoImage(file="images\sprocket150.png")
        self.w = Label(window, image=self.photo, bg='#024889')
        self.w.photo = self.photo
        self.w.place(x=10, y=10)

        self.vaxLabel = Label(self, font=("Tahoma", 26), fg='#fcd200', bg = '#024889', text = "What's going on in the VAX?")
        self.vaxLabel.place(x=410, y=150, anchor="center")

        self.eventVar = StringVar()
        self.eventLabel = Label(self, font=("Tahoma", 26), fg='#fcd200', bg = '#024889')
        self.eventLabel.place(x=400, y=250, anchor="center")
        self.eventLabel["textvariable"] = self.eventVar

        self.timeVar = StringVar()
        self.timeLabel = Label(self, font=("Tahoma", 20), fg='#fcd200', bg = '#024889')
        self.timeLabel.place(x=400,y=320, anchor="center")
        self.timeLabel["textvariable"] = self.timeVar

        self.clockVar = StringVar()
        self.clockLabel = Label(self, font=("Tahoma", 14), fg='#fcd200', bg='#024889')
        self.clockLabel.place(x=690, y=460, anchor="center")
        self.clockLabel["textvariable"] = self.clockVar

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        # Updates the display
        displayStr = updateEvent()
        self.eventVar.set(displayStr[0])
        self.timeVar.set(displayStr[1])
        now = datetime.now()
        hour = int(now.strftime('%H'))
        if (hour > 12):  # Determine if the Start Time is AM or PM
            ampm = " PM - "
            hour -= 12
        else:
            ampm = " AM - "
        self.clockVar.set(str(hour) + ":" + now.strftime("%M:%S") + ampm + now.strftime("%m/%d/%Y"))
        self.after(250, self.onUpdate) # Loop update

window = Tk()
window.title("VAX Reservation Display")
window.geometry("800x480")
window.config(bg = '#024889')
window.overrideredirect(True) # removes title bar
app = Application(master=window)
window.mainloop()