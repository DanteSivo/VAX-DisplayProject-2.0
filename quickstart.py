from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def getEvents():
    """Shows basic usage of the Google Calendar API.
    Modified by Dante Sivo
    Returns the data next 3 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    return events;

def vaxCheck(eventList):
    vaxEvents = []
    for index in range(len(eventList)):
        summary = eventList[index].get('summary')
        if (summary != None):
            if ((summary.find("VAX") >= 0) or (summary.find("vax") >= 0) or (summary.find("Vax") >= 0)): # If the word VAX is in the title
                    vaxEvents.append(eventList[index])
                    continue
        location = eventList[index].get('location')
        if (location != None):
            if ((location.find("VAX") >= 0) or (location.find("vax") >= 0) or (location.find("Vax") >= 0)):
                    vaxEvents.append(eventList[index])
                    continue
    return vaxEvents

def main():
    eventsList = vaxCheck(getEvents())   # Return an array of the next 3 upcoming events. (The Current / Ongoing, and the future 2).
    for event in eventsList:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    return eventsList

main()