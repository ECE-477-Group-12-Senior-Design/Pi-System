# Setup.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# September 21, 2021
#

# Download the helper library from https://www.twilio.com/docs/python/install

import os
from twilio.rest import Client
from SMSAlert.Constants import *
from SMSAlert.NotificationManager import NotificationManager


def setup(username, name, phoneNumber):
    __setUsername(username)
    __setEmergencyPhoneNumber(name, phoneNumber)
    __sendTestMessage()


def __setUsername(username):
    os.environ[TWILIO_USER_NAME] = username


def __setEmergencyPhoneNumber(name, phoneNumber):
    # Check only numbers
    if int(phoneNumber) is None:
        print("Implement not only numbers error")

    # Check if 10 digits
    if len(phoneNumber) != 10:
        print("Implement is not 10 digits error")

    # Check if first digit is 1
    if phoneNumber[0] == 1:
        print("Implement first digit is 1 error")

    # Format phone number
    phoneNumber = '+1' + phoneNumber

    # Set environment variables
    os.environ[TWILIO_CONTACT_NAME] = name
    os.environ[TWILIO_CONTACT_NUMBER] = phoneNumber


def __sendTestMessage():
    contact_name = os.environ[TWILIO_CONTACT_NAME]
    body = TWILIO_FORMATTED_TEST_SMS.format(contact_name)

    notificationManager = NotificationManager()
    notificationManager.send_message(body)
