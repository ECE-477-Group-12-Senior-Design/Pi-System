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
from random import randrange # TODO: Remove this for real version
from SMSAlert.SetupEnvironment import set_environment_variables
from DEBUG import DEBUG

WINDOW_SIZE = 50

def mock():
    if not DEBUG:
        raise Exception("Main.mock() should not be used unless DEBUG mode enabled!")
        
    upper_bound = 50
    x_accel = randrange(upper_bound)
    y_accel = randrange(upper_bound)
    z_accel = randrange(upper_bound)
    x_gyro = randrange(upper_bound)
    y_gyro = randrange(upper_bound)
    z_gyro = randrange(upper_bound)
    return [x_accel, y_accel, z_accel, x_gyro, y_gyro, z_gyro]

def get_current_values():
    if DEBUG:
        return [mock() for _ in range(WINDOW_SIZE)]
    else:
        raise Exception("get_current_values not implemented!")

def main():
    if DEBUG:
        set_environment_variables()
        
    while True:
        sleep(1)
        values = get_current_values()
        is_fall = FallDetector.determine_if_fall(values)
        
        if is_fall:
            print('\n*** ALERT: THIS IS A FALL! ***')
            EmergencyAlert.sendEmergencyAlert()
            print('*** EMERGENCY ALERT SENT! ***\n')
            return # TODO: Handle logic when fall
        else:
            print('Not a Fall')  

if __name__ == '__main__':
    main()
    