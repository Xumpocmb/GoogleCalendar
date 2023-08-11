import datetime as dt
import json
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            print(f'{token}')
    return creds


def get_events():
    try:
        service = build('calendar', 'v3', credentials=creds)
        now = dt.datetime.utcnow().isoformat() + 'Z'

        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()

        with open('events_result.json', 'w') as file:
            json.dump(events_result, file)

        events = events_result.get('items', [])
        with open('events.json', 'w') as file:
            json.dump(events, file)

        if not events:
            print('No upcoming events found.')
            return

        with open('events-list.txt', 'w', encoding='utf-8') as file:
            for event in events:
                info = event.get('summary', None)
                start = event['start'].get('dateTime', None)
                print(start, event['summary'])
                file.write(f'{start}\n')
                print('*' * 30)

    except HttpError as e:
        print(e)


def create_event():
    try:
        service = build('calendar', 'v3', credentials=creds)
        event = {
            'summary': 'test003',
            'location': '800 Howard St., San Francisco, CA 94103',
            'description': 'A chance to hear more about Google developer products.',
            'start': {
                'dateTime': '2023-08-11T10:00:00+03:00',
                'timeZone': 'Europe/Minsk',
            },
            'end': {
                'dateTime': '2023-08-11T11:00:00+03:00',
                'timeZone': 'Europe/Minsk',
            },
            'attendees': [
                {'email': 'lpage@example.com'},
                {'email': 'sbrin@example.com'},
            ],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f'event created {event.get("htmlLink")}')

    except HttpError as e:
        print(e)


def empty_func():
    print('-' * 30)


if __name__ == '__main__':
    creds = main()
    while True:
        print('1 - list')
        print('2 - create')
        choice = input('type: ')
        match choice:
            case '1':
                get_events()
            case '2':
                create_event()
            case '3':
                empty_func()
            case _:
                break

