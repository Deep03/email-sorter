import base64
import email
import json
test_id = ''
str = "---------"


# def base64_decode(data):
#     msg_str = base64.urlsafe_b64decode(data.encode("utf-8")).decode("utf-8")
#     return msg_str


# print(base64_decode(str))

try:
    with open('data/msgs.json', 'r') as msg_file:
        msg_data = json.load(msg_file)
    msg_file.close()
except Exception as e:
    with open('data/msgs.json', 'w+') as msg_file:
        print("Error Here")
        test_data  = {'msg_strs': [], 'msg_ids': []}
        json.dump(test_data, msg_file, indent=4)
    msg_file.close()
