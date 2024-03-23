from google.oauth2 import service_account

from dotenv import find_dotenv, load_dotenv
import googleapiclient.discovery

import os

load_dotenv(find_dotenv(), override=True)

SCOPES = ["https://mail.google.com/"]
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE_PATH")

subject = "Abdullah@monhna.com"
credentials = service_account.Credentials.from_service_account_file(
    filename=SERVICE_ACCOUNT_FILE, scopes=["https://mail.google.com/"], subject=subject
)

gmail_service = googleapiclient.discovery.build("gmail", "v1", credentials=credentials)


def get_otp():
    try:
        all_messages = gmail_service.users().messages().list(userId="me").execute()
        if all_messages:
            last_message_id = all_messages["messages"][0]["id"]
            try:
                last_message = (
                    gmail_service.users()
                    .messages()
                    .get(userId="me", id=last_message_id, format="metadata")
                    .execute()
                )
                otp = last_message["snippet"][:6]
                return otp
            except Exception as error:
                print("An error occurred: %s" % error)
    except Exception as error:
        print("An error occurred: %s" % error)


print(get_otp())
