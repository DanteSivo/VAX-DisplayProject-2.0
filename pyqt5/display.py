# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'displayDesign.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
from threading import Thread
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setStyleSheet("background-color: rgb(2, 72, 137);")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Make frameless
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/sprocket150.png"))
        self.label.setObjectName("label")
        self.vaxLabel = QtWidgets.QLabel(self.centralwidget)
        self.vaxLabel.setGeometry(QtCore.QRect(200, 30, 511, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.vaxLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.vaxLabel.setFont(font)
        self.vaxLabel.setAcceptDrops(False)
        self.vaxLabel.setAutoFillBackground(True)
        self.vaxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.vaxLabel.setObjectName("vaxLabel")
        self.eventLabel = QtWidgets.QLabel(self.centralwidget)
        self.eventLabel.setGeometry(QtCore.QRect(200, 140, 511, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.eventLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eventLabel.setFont(font)
        self.eventLabel.setAcceptDrops(False)
        self.eventLabel.setAutoFillBackground(False)
        self.eventLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.eventLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.eventLabel.setObjectName("eventLabel")
        self.eventTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.eventTimeLabel.setGeometry(QtCore.QRect(200, 210, 511, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.eventTimeLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eventTimeLabel.setFont(font)
        self.eventTimeLabel.setAcceptDrops(False)
        self.eventTimeLabel.setAutoFillBackground(False)
        self.eventTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.eventTimeLabel.setObjectName("eventTimeLabel")
        self.upcomingEventLabel = QtWidgets.QLabel(self.centralwidget)
        self.upcomingEventLabel.setGeometry(QtCore.QRect(200, 300, 511, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.upcomingEventLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.upcomingEventLabel.setFont(font)
        self.upcomingEventLabel.setAcceptDrops(False)
        self.upcomingEventLabel.setAutoFillBackground(False)
        self.upcomingEventLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.upcomingEventLabel.setObjectName("upcomingEventLabel")
        self.upcomingTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.upcomingTimeLabel.setGeometry(QtCore.QRect(200, 370, 511, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 210, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 72, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.upcomingTimeLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.upcomingTimeLabel.setFont(font)
        self.upcomingTimeLabel.setAcceptDrops(False)
        self.upcomingTimeLabel.setAutoFillBackground(False)
        self.upcomingTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.upcomingTimeLabel.setObjectName("upcomingTimeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loop = 0
        thread = Thread(target=self.update_text, args=(MainWindow,))
        thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vaxLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fcd200;\">vaxLabel</span></p></body></html>"))
        self.eventLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fcd200;\">eventLabel</span></p></body></html>"))
        self.eventTimeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fcd200;\">eventTimeLabel</span></p></body></html>"))
        self.upcomingEventLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fcd200;\">upcomingEventLabel</span></p></body></html>"))
        self.upcomingTimeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fcd200;\">upcomingTimeLabel</span></p></body></html>"))

    def update_text(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        while True:
            eventDisplayStr = updateEvent()
            self.eventLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fcd200;\">"
                                                            + eventDisplayStr[0] +
                                                            "</span></p></body></html>"))
            self.eventTimeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fcd200;\">"
                                                            + eventDisplayStr[1] +
                                                            "</span></p></body></html>"))
            #global counterex
            upcomingDisplayStr = updateUpcoming()
            self.upcomingEventLabel.setText(_translate("MainWindow","<html><head/><body><p><span style=\" color:#fcd200;\">"
                                                            + upcomingDisplayStr[0] +
                                                            "</span></p></body></html>"))
            self.upcomingTimeLabel.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" color:#fcd200;\">"
                                                            + upcomingDisplayStr[1] +
                                                            "</span></p></body></html>"))

            self.vaxLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fcd200;\">"
                                                           + str(self.loop) +"</span></p></body></html>"))
            self.loop += 1
            sleep(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
