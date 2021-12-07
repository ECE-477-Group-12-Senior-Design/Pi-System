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
from FallDetection.FallDetector import FallDetector
from SMSAlert.EmergencyAlert import EmergencyAlert
from random import randrange  # TODO: Remove this for real version
from SMSAlert.SetupEnvironment import set_environment_variables
from Debug.DEBUG import *
from SMSAlert.BatteryAlert import BatteryAlert
import FallDetection.DataParsing as parse
from posixpath import split
from bluepy.btle import UUID, Peripheral, DefaultDelegate
import datetime
import numpy as np


class PiBluetoothDelegate(DefaultDelegate):

    def __init__(self):
        DefaultDelegate.__init__(self)
        self.running = True
        self.stored_data = []

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

        if parse.detect_junk(spaced_str) == 0:
            print(spaced_str)
            self.stored_data.append(spaced_str)

        if spaced_str.count('0e') > 10:
            self.running = False
            print("storing data")
            dat = parse.generate_array(self.stored_data)
            all_axes = parse.acceleration_data(dat)

            parse.plot_data(all_axes[0], 'x_accel.png')
            parse.plot_data(all_axes[1], 'y_accel.png')
            parse.plot_data(all_axes[2], str(str(dt)[22:]) + 'z_accel.png')

            combined_x_y_z = [all_axes[0], all_axes[1], all_axes[2]] # TODO: Only accel
            result = FallDetector.determine_if_fall(combined_x_y_z)
            print(f"FALL?: {result}")

            np.savetxt("data_test.csv", all_axes, delimiter=',', fmt='%.8f')
            # determine_if_fall([])
            # Send stored_data array to Fall Detection Algo
            self.stored_data = []


class PiSystem:
    WINDOW_SIZE = 50

    # Bluetooth
    SERVICE_UUID = '0000f00d-1212-efde-1523-785fef13d123'
    CHARACTERISTIC_UUID = '0000beef-1212-efde-1523-785fef13d123'
    MICROCONTROLLER_MAC = "c6:a6:ac:8f:47:b1"
    outputData = []

    peripheral: Peripheral
    svc = None  # TODO: Determine type
    ch = None  # TODO: Determine type

    def configure_bluetooth(self):
        self.peripheral = Peripheral(self.MICROCONTROLLER_MAC, "random")
        delegate = PiBluetoothDelegate()
        self.peripheral.setDelegate(delegate)

        self.svc = self.peripheral.getServiceByUUID(self.SERVICE_UUID)
        self.ch = self.svc.getCharacteristics()[0]
        self.p.writeCharacteristic(int(self.ch.valHandle) + 1, b'\x01\x00')

    def main(self):
        if MAIN_DEBUG:
            set_environment_variables()

        if MAIN_DEBUG and TEST_LOW_BATTERY:
            BatteryAlert.sendLowBatteryAlert()

        if MAIN_DEBUG and TEST_HIGH_BATTERY:
            BatteryAlert.sendFullBatteryAlert()

        while True:
            sleep(1)

            if self.peripheral.waitForNotifications(1):
                # handleNotification() was called
                continue

            # is_fall = FallDetector.determine_if_fall(values)

            # if is_fall:
            #     print('\n*** ALERT: THIS IS A FALL! ***')
            #     EmergencyAlert.sendEmergencyAlert()
            #     print('*** EMERGENCY ALERT SENT! ***\n')
            #     return  # TODO: Handle logic when fall
            # else:
            #     print('Not a Fall')


if __name__ == '__main__':
    PiSystem().main()
