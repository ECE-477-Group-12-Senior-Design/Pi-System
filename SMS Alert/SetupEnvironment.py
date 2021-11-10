# SetupEnvironment.py

import os
from Constants import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

def set_environment_variables():
    os.environ[TWILIO_ACCOUNT_SID] = "AC96b41009f986d4e51b628b7e453f1421"
    os.environ[TWILIO_AUTH_TOKEN] = "1a159010a8195c0649da24e65eb9965a"
    print("Twilio environment variables set!")
