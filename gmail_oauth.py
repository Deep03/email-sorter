# necessary libraries
from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json, base64, email, time

# DO NOT EDIT THE FOLLOWING:
class CredsUser:
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
        try:
            service = build('gmail', 'v1', credentials=creds)
        except:
            creds.refresh(Request())
            service = build('gmail', 'v1', credentials=creds)
        return service
client = CredsUser()
service = client.get_creds()

# END OF DO NOT EDIT

class UserDetail():

    @classmethod
    def get_label(cls):
        try:
            results = service.users().labels().list(userId='me').execute()
            labels = results.get('labels', [])
        except Exception as error:
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


    
    @classmethod
    def get_msg(cls):

        # users.messages.list from Gmail api || change maxResults to 500 after test
        emails = service.users().messages().list(userId='me', **{'maxResults': 5}).execute()
        
        # to get specific email id, ex: ["ex1": [], .... ["id": "231313213"]....]
        ids_json = emails.get('messages', [])

        # to save the ids into msgs.json file
        try:
            with open('data/msgs.json', 'r') as msg_file:
                exst_data = json.load(msg_file)
            msg_file.close()
        except Exception as e:
            with open('data/msgs.json', 'w+') as msg_file:
                exst_data  = {
                    'msg_strs': [],
                    'msg_ids': []
                    }
                json.dump(exst_data, msg_file, indent=4)
            msg_file.close()
            
        with open('data/msgs.json', 'a') as msg_file:
            for dict_id in ids_json:
                id_value = dict_id['id']
                body_msg = service.users().messages().get(userId='me', id=id_value, format='raw').execute()
                msg_str = base64.urlsafe_b64decode(body_msg['raw'].encode("utf-8")).decode("utf-8")
                mime_msg = email.message_from_string(msg_str)
                def get_email_body(message):
                    for part in message.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            try:
                                return part.get_payload(decode=True).decode(part.get_content_charset(), 'ignore')
                            except Exception as e:
                                return "null"
                
                msg = get_email_body(mime_msg)
                if msg not in exst_data["msg_strs"]:
                    print("true")
                    exst_data["msg_strs"].append(msg)
                else:
                    print("false")
                if id_value not in exst_data['msg_ids']:
                    print("true")
                    exst_data["msg_ids"].append(id_value)
                else:
                    print("false")
        msg_file.close()

# append mode appends instead of writing, temp solution
        with open('data/msgs.json', 'w') as f:
            json.dump(exst_data, f, indent=4)
        f.close()


user_data = UserDetail()

# function to get labels
user_data.get_label()


# function to get messages
user_data.get_msg()

