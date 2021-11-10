# NotificationManager.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# October 01, 2021
#

import os
from twilio.rest import Client
from SMSAlert.Constants import *

class NotificationManager:

    __client: Client

    def __init__(self) -> None:
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure

        account_sid = os.environ[TWILIO_ACCOUNT_SID]
        auth_token = os.environ[TWILIO_AUTH_TOKEN]
        self.__client = Client(account_sid, auth_token)

    def send_message(self, message: str) -> str:
        _from = TWILIO_FROM_NUMBER
        _to = os.environ[TWILIO_CONTACT_NUMBER]

        message = self.__client.messages.create(body=message, from_=_from, to=_to)
        return message.sid


