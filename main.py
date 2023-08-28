from __future__ import print_function

import os.path, email
import base64

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

        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}') 

    # data entry in data/label_data.json --- -- to be writtten into a function
    with open('data/label_data.json', 'r') as json_file:
        ex_data = json.load(json_file)
    json_file.close()
    with open('data/label_data.json', 'w+') as json_file:
        for label in labels:
            l_name = label['name']
            l_id = label['id']
            # efficient file entry
            if l_name not in ex_data['label_names']:
                ex_data["label_names"].append(l_name)
            if l_id not in ex_data['label_ids']:
                ex_data["label_ids"].append(l_id)
        json.dump(ex_data, json_file, indent=4)
    json_file.close()

    # # data entry for msgs.json(msg_id) -- to be writtten into a function
    # emails = service.users().messages().list(userId='me', **{'maxResults': 500}).execute()
    # msgs = emails.get('messages', [])

    # with open('data/msgs.json', 'r') as msg_file:
    #     exst_data = json.load(msg_file)
    # msg_file.close()
    # with open('data/msgs.json', 'w+') as msg_file:
    #     for dict_id in msgs:
    #         id_value = dict_id['id']
    #         if id_value not in exst_data['msg_ids']:
    #             exst_data["msg_ids"].append(id_value)
    #     json.dump(exst_data, msg_file, indent=4)
    # msg_file.close()

    # # data entry for msgs.json(msg_strs) -- to be writtten into a function
    # with open('data/msgs.json', 'r') as msg_file:
    #     msg_data = json.load(msg_file)
    # msg_file.close()
    # with open('data/msgs.json', 'w+') as msg_file:
    #     for msg_id in msg_data['msg_ids']:
    #         body_message = service.users().messages().get(userId='me', id=msg_id, format='raw').execute()
    # msg_file.close()

    def base64_decode(data):
        msg_str = base64.urlsafe_b64decode(data)
        return msg_str

            
if __name__ == '__main__':
    main()