# EmergencyAlert.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# October 01, 2021
#

import os
from SMSAlert.Constants import *
from SMSAlert.NotificationManager import *


class EmergencyAlert:

    @staticmethod
    def sendEmergencyAlert() -> None:
        user_name = os.environ[TWILIO_USER_NAME]
        print('USERNAME:', user_name)
        body = TWILIO_FORMATTED_EMERGENCY_SMS.format(user_name)

        notificationManager = NotificationManager()
        notificationManager.send_message(body)
