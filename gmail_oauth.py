# necessary libraries
from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json




class GmailApi:

    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',	
    'https://www.googleapis.com/auth/gmail.labels',	
    "https://www.googleapis.com/auth/gmail.send",	
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.insert",	
    "https://www.googleapis.com/auth/gmail.modify",		
    "https://www.googleapis.com/auth/gmail.settings.basic",	
    "https://www.googleapis.com/auth/gmail.settings.sharing"]

    @classmethod
    def get_creds(cls):
        creds = None
        if os.path.exists('data/token.json'):
            creds = Credentials.from_authorized_user_file('data/token.json', cls.SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('data/credentials.json', cls.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('data/token.json', 'w') as token:
                token.write(creds.to_json())
        return creds


client = GmailApi()
creds = client.get_creds()
print(creds)



