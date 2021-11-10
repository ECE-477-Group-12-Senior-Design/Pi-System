# EmergencyAlert.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# October 01, 2021
#

import os
from Constants import *
from NotificationManager import *


class EmergencyAlert:

    def sendEmergencyAlert() -> None:
        user_name = os.environ[TWILIO_USER_NAME]
        body = TWILIO_USER_NAME.format(user_name)

        notificationManager = NotificationManager()
        notificationManager.send_message(body)
