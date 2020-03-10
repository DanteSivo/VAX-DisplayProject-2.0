from tkinter import *
import quickstart
from datetime import datetime
global counterex

def updateEvent():
    eventsList = quickstart.main()
    if (len(eventsList) <= 0):
       return ["No events ongoing or planned!", ""]
   # There must be at least 1 event in the calendar

    event = eventsList[0] # Are any of these events going on in the VAX???
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

def updateUpcoming():
    eventsList = quickstart.main()
    if (len(eventsList) <= 2):
        return ["", ""]
    # There must be at least 2 events in the calendar
    event = eventsList[1]
    if (event == None):
        return ["No events planned", ""]

    start = event['start'].get('dateTime', event['start'].get('date')).split('T')  # basic parsing
    startDate = start[0].split('-')  # Start date of the event Y/M/D format
    startTime = start[1].split(':')  # H/M/timeZone/S format
    end = event['end'].get('dateTime', event['start'].get('date')).split('T')  # basic parsing
    endDate = end[0].split('-')  # End date of the event Y/M/D format
    endTime = end[1].split('-')  # End time of the event
    endTime = endTime[0].split(':')  # H/M/S format
    eventOngoing = isEventOngoing(startTime, startDate, endTime, endDate)

    getTimeDisplay = timeParse(startTime, endTime)
    getEventDisplay = eventParse(eventsList[1].get('summary'))

    if (eventOngoing):
        # Update label text to show the event in ongoing
        return ["Also going on: " + getEventDisplay, getTimeDisplay]
    # if the event is in the future
    return ["Upcoming: " + getEventDisplay, getTimeDisplay + ' ' + endDate[1] + '/' + endDate[2] + '/' + endDate[0]]

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
    if (startHour == 0):
        startHour = 12
    if (endHour == 0):
        endHour = 12
    return str(startHour) + ':' + startTime[1] + startM  + " - " + str(endHour) + ':' + endTime[1] + endM + ' -'

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
        global counterex
        self.frame = Frame.__init__(self, master, width = 800, height = 480, bg = '#024889')
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.photo = PhotoImage(file="../images/sprocket150.png")
        self.w = Label(window, image=self.photo, bg='#024889')
        self.w.photo = self.photo
        self.w.place(x=10, y=10)

        self.vaxLabel = Label(self, font=("Tahoma", 26), fg='#fcd200', bg = '#024889', text = "What's going on in the VAX?")
        self.vaxLabel.place(x=410, y=130, anchor="center")

        self.eventVar = StringVar()
        self.eventLabel = Label(self, font=("Tahoma", 20), fg='#fcd200', bg = '#024889')
        self.eventLabel.place(x=400, y=230, anchor="center")
        self.eventLabel["textvariable"] = self.eventVar

        self.eventTimeVar = StringVar()
        self.eventTimeLabel = Label(self, font=("Tahoma", 16), fg='#fcd200', bg = '#024889')
        self.eventTimeLabel.place(x=400,y=280, anchor="center")
        self.eventTimeLabel["textvariable"] = self.eventTimeVar

        self.upcomingEventVar = StringVar()
        self.upcomingEventLabel = Label(self, font=("Tahoma", 20), fg='#fcd200', bg='#024889')
        self.upcomingEventLabel.place(x=400, y=350, anchor="center")
        self.upcomingEventLabel["textvariable"] = self.upcomingEventVar

        self.upcomingTimeVar = StringVar()
        self.upcomingTimeLabel = Label(self, font=("Tahoma", 16), fg='#fcd200', bg='#024889')
        self.upcomingTimeLabel.place(x=400, y=400, anchor="center")
        self.upcomingTimeLabel["textvariable"] = self.upcomingTimeVar

        # initial time display
        self.onUpdate()


    def onUpdate(self):
        # Updates the display
        eventDisplayStr = updateEvent()
        self.eventVar.set(eventDisplayStr[0])
        self.eventTimeVar.set(eventDisplayStr[1])
        global counterex
        upcomingDisplayStr = updateUpcoming()
        self.upcomingEventVar.set(upcomingDisplayStr[0])
        self.upcomingTimeVar.set(upcomingDisplayStr[1])
        try:
            if counterex > 10: # Crash every 10 minuets
                raise SystemExit
            counterex += 1
        except NameError:
            counterex = 0
        self.after(1000, self.onUpdate)  # Loop update - per 2 minutes

window = Tk()
window.title("VAX Reservation Display")
window.geometry("800x480")
window.config(bg = '#024889')
window.overrideredirect(True) # removes title bar
app = Application(master=window)
window.mainloop()