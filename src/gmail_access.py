from google.oauth2 import service_account

from dotenv import find_dotenv, load_dotenv
import googleapiclient.discovery

import os

load_dotenv(find_dotenv(), override=True)

SCOPES = ["https://mail.google.com/"]
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE_PATH")

# this way of creating the credentials object does not work
# credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# delegated_credentials = credentials.with_subject('Abdullah@baghwita.com')

# This way works
subject = "Abdullah@monhna.com"
credentials = service_account.Credentials.from_service_account_file(
    filename=SERVICE_ACCOUNT_FILE, scopes=["https://mail.google.com/"], subject=subject
)

gmail_service = googleapiclient.discovery.build("gmail", "v1", credentials=credentials)
# response = gmail_service.users().getProfile(userId="me").execute()
# response = gmail_service.users().messages().list(userId="me").execute()

import base64
import email

def get_all_messages(service, user_id):
  pass


def get_last_message(service, user_id):
  try:
    all_messages=service.users().messages().list(userId=user_id).execute()
    if all_messages:
      last_message_id=all_messages['messages'][0]["id"]
      try:
        last_message= service.users().messages().get(userId=user_id, id=last_message_id, format='metadata').execute()
        return last_message
      except Exception as error:
        print('An error occurred: %s' % error)
  except Exception as error:
    print('An error occurred: %s' % error)

last_message=get_last_message(gmail_service,'me')

def get_otp(last_message):
  return last_message["snippet"][:6]
otp=get_otp(last_message)
print(otp)


def get_mime_message(service, user_id, msg_id):
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()
    print('Message snippet: %s' % message['snippet'])
    msg_str = base64.urlsafe_b64decode(message['raw'].encode("utf-8")).decode("utf-8")
    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except Exception as error:
    print('An error occurred: %s' % error)