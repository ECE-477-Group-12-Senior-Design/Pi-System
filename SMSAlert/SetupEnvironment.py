#!/usr/bin/env python3

# SetupEnvironment.py

import os
from SMSAlert.Constants import *
from DEBUG import DEBUG

def set_environment_variables():
    os.environ[TWILIO_ACCOUNT_SID] = "AC96b41009f986d4e51b628b7e453f1421"
    os.environ[TWILIO_AUTH_TOKEN] = "1a159010a8195c0649da24e65eb9965a"

    if DEBUG:
        os.environ[TWILIO_CONTACT_NAME] = "Charles"
        os.environ[TWILIO_CONTACT_NUMBER] = "+19739179742"
        os.environ[TWILIO_USER_NAME] = "Alia"
        print('DEBUG environment varibales set!')

    print("Twilio environment variables set!")
