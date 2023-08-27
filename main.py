from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',	
'https://www.googleapis.com/auth/gmail.labels',	
"https://www.googleapis.com/auth/gmail.send",	
"https://www.googleapis.com/auth/gmail.compose",
"https://www.googleapis.com/auth/gmail.insert",	
"https://www.googleapis.com/auth/gmail.modify",	
"https://www.googleapis.com/auth/gmail.metadata",	
"https://www.googleapis.com/auth/gmail.settings.basic",	
"https://www.googleapis.com/auth/gmail.settings.sharing"]

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('data/token.json'):
        creds = Credentials.from_authorized_user_file('data/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'data/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('data/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        emails = service.users().messages().list(userId='me').execute()
        msgs = emails.get('messages', [])
        keys_list = []
        for dict_id in msgs:
            id_value = dict_id['id']
            keys_list.append(id_value)
        # Specify message IDs to modify
        # message_ids = keys_list

        # # Specify label IDs to add and remove
        # labels_to_add = ['Label_6']  # Replace with actual label IDs
        # labels_to_remove = [""]  # Replace with actual label IDs

        # # Construct modify request body
        # modify_body = {
        #     "addLabelIds": labels_to_add,
        # }
        # try:
        #     response = service.users().messages().modify(userId='me', id="18a06f5692a26bfb", body=modify_body).execute()
        # except HttpError as error:
        # # TODO(developer) - Handle errors from gmail API.
        #     print(f'An error occurred: {error}')

        results = service.users().labels().list(userId='me').execute()

        labels = results.get('labels', [])
        with open('data/label_data.json', 'r') as json_file:
            ex_data = json.load(json_file)
        json_file.close()
        with open('data/label_data.json', 'w+') as json_file:
            for label in labels:
                l_name = label['name']
                l_id = label['id']
                # efficient file entry
                if l_name not in ex_data['label_name']:
                    ex_data["label_name"].append(l_name)
                if l_id not in ex_data['label_id']:
                    ex_data["label_id"].append(l_id)
            json.dump(ex_data, json_file, indent=4)
        json_file.close()



    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()