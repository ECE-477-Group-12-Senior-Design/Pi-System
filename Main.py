#!/usr/bin/env python3

# Main.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# November 10, 2021
#

from math import isfinite
from time import sleep
from FallDetection.FallDetector import determine_if_fall
from SMSAlert.EmergencyAlert import EmergencyAlert
from random import randrange  # TODO: Remove this for real version
from SMSAlert.SetupEnvironment import set_environment_variables
from Debug.DEBUG import *
from SMSAlert.BatteryAlert import BatteryAlert
import FallDetection.DataParsing as parse
from posixpath import split
from bluepy.btle import UUID, Peripheral, DefaultDelegate
import bluepy
import datetime
import numpy as np
import math
from SMSAlert.BluetoothAlert import BluetoothAlert


class PiBluetoothDelegate(DefaultDelegate):

    def __init__(self, handle_fall):
        DefaultDelegate.__init__(self)
        self.running = True
        self.stored_data = []
        self.handle_fall = handle_fall

    def handleNotification(self, cHandle, data):
        # Process data and store into array
        # print(data)
        hexString = data.hex()
        # print(hexString)
        # print("LENGTH: ", len(hexString))
        dt = (datetime.datetime.now())
        # print("\n")

        splitNum = int(len(hexString) / 6)
        step = splitNum
        # print(splitNum)

        # print(str(hexString))

        spaced_str = hexString[0:2] + ' ' + hexString[2:4] + ' ' + hexString[4:6] + ' ' + \
                     hexString[6:8] + ' ' + hexString[8:10] + ' ' + hexString[10:12] + ' ' + \
                     hexString[12:14] + ' ' + hexString[14:16] + ' ' + hexString[16:18] + ' ' + \
                     hexString[18:20] + ' ' + hexString[20:22] + ' ' + hexString[22:24] + ' ' + \
                     hexString[24:26] + ' ' + hexString[26:28] + ' ' + hexString[28:30] + ' ' + \
                     hexString[30:32] + ' ' + hexString[32:34] + ' ' + hexString[34:36] + ' ' + \
                     hexString[34:36] + ' ' + hexString[36:38] + ' ' + hexString[38:]

        print(spaced_str)

        if spaced_str.count('0e') > 10:
            # self.running = False
            print("storing data")
            dat = parse.generate_array(self.stored_data)
            all_axes = parse.acceleration_data(dat)

            parse.plot_data(all_axes[0], 'x_accel.png')
            parse.plot_data(all_axes[1], 'y_accel.png')
            parse.plot_data(all_axes[2], str(str(dt)[22:]) + 'z_accel.png')

            combined_x_y_z = [all_axes[0], all_axes[1], all_axes[2]]  # TODO: Only accel

            did_fall = determine_if_fall(combined_x_y_z)

            if did_fall:
                pass
                # Detected a fall
                # TODO: Uncomment next line to send text messages
                # self.handle_fall()

            print(f"FALL?: {did_fall}")

            # determine_if_fall([])
            # Send stored_data array to Fall Detection Algo
            self.stored_data = []
        elif parse.detect_junk(spaced_str) == 0:
            self.stored_data.append(spaced_str)
        elif parse.detect_battery(spaced_str) == 1:
            print(spaced_str)
            parse.notify_battery(hexString[20:22], hexString[22:24])
        else:
            print("invalid data string")
            # print(spaced_str)


class PiSystem:
    # Bluetooth
    SERVICE_UUID = '0000f00d-1212-efde-1523-785fef13d123'
    CHARACTERISTIC_UUID = '0000beef-1212-efde-1523-785fef13d123'
    MICROCONTROLLER_MAC = "f9:55:32:07:a4:9e"
    # MICROCONTROLLER_MAC = "c6:a6:ac:8f:47:b1"
    outputData = []

    peripheral: Peripheral
    svc = None  # TODO: Determine type
    ch = None  # TODO: Determine type

    def main(self):
        if MAIN_DEBUG:
            set_environment_variables()

        if MAIN_DEBUG and TEST_LOW_BATTERY:
            BatteryAlert.sendLowBatteryAlert()

        if MAIN_DEBUG and TEST_HIGH_BATTERY:
            BatteryAlert.sendFullBatteryAlert()
        
        def connectDevice():
            self.peripheral = Peripheral(self.MICROCONTROLLER_MAC, "random")
            delegate = PiBluetoothDelegate(handle_fall=EmergencyAlert.sendEmergencyAlert)
            self.peripheral.setDelegate(delegate)
            print("Device Connected")
        
        def subscribeToNotifications():
            self.svc = self.peripheral.getServiceByUUID(self.SERVICE_UUID)
            self.ch = self.svc.getCharacteristics()[0]
            self.peripheral.writeCharacteristic(int(self.ch.valHandle) + 1, b'\x01\x00')
            print("Subscribed to notifications")
        
        while True:
            
            try:
                connectDevice()
                subscribeToNotifications()
                BluetoothAlert.sendConnectedAlert()
                
                if self.peripheral.waitForNotifications(1):
                    # handleNotification() is called
                    continue
            except bluepy.btle.BTLEDisconnectError as e:
                print("ERROR: " + str(e) + " ...Attempting to reconnect")
                BluetoothAlert.sendDisconnectedAlert()
            except Exception as err:
                print(err)
                BluetoothAlert.sendUnexpectedAlert(str(err))


if __name__ == '__main__':
    PiSystem().main()
