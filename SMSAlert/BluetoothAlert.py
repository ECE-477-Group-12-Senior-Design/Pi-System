# BluetoothAlert.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# December 10, 2021
#

from SMSAlert.NotificationManager import *


class BluetoothAlert:

    @staticmethod
    def sendConnectedAlert() -> None:
        notificationManager = NotificationManager()
        notificationManager.send_message(TWILIO_BLUETOOTH_CONNECTED_SMS)

    @staticmethod
    def sendDisconnectedAlert() -> None:
        notificationManager = NotificationManager()
        notificationManager.send_message(TWILIO_BLUETOOTH_DISCONNECTED_SMS)
