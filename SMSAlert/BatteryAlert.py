# BatteryAlert.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# December 01, 2021
#

import os
from SMSAlert.Constants import *
from SMSAlert.NotificationManager import *


class BatteryAlert:

    @staticmethod
    def sendLowBatteryAlert() -> None:
        contact_name = os.environ[TWILIO_CONTACT_NAME]
        user_name = os.environ[TWILIO_USER_NAME]
        
        body = TWILIO_FORMATTED_LOW_BATTERY_SMS.format(contact_name=contact_name, user_name=user_name)

        notificationManager = NotificationManager()
        notificationManager.send_message(body)

    @staticmethod
    def sendBatteryChargingAlert() -> None:
        contact_name = os.environ[TWILIO_CONTACT_NAME]
        user_name = os.environ[TWILIO_USER_NAME]

        body = TWILIO_FORMATTED_CHARGING_BATTERY_SMS.format(contact_name=contact_name, user_name=user_name)

        notificationManager = NotificationManager()
        notificationManager.send_message(body)

    @staticmethod
    def sendFullBatteryAlert() -> None:
        contact_name = os.environ[TWILIO_CONTACT_NAME]
        user_name = os.environ[TWILIO_USER_NAME]
        
        body = TWILIO_FORMATTED_FULL_BATTERY_SMS.format(contact_name=contact_name, user_name=user_name)

        notificationManager = NotificationManager()
        notificationManager.send_message(body)

    @staticmethod
    def sendBatteryFaultAlert() -> None:
        contact_name = os.environ[TWILIO_CONTACT_NAME]
        user_name = os.environ[TWILIO_USER_NAME]

        body = TWILIO_FORMATTED_BATTERY_FAULT_SMS.format(contact_name=contact_name, user_name=user_name)

        notificationManager = NotificationManager()
        notificationManager.send_message(body)
