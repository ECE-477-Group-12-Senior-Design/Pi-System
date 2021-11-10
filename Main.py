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

def mock():
    if not DEBUG:
        raise Exception("Main.mock() should not be used unless DEBUG mode enabled!")
        
    upper_bound = 70
    x_accel = randrange(upper_bound)
    y_accel = randrange(upper_bound)
    z_accel = randrange(upper_bound)
    x_gyro = randrange(upper_bound)
    y_gyro = randrange(upper_bound)
    z_gyro = randrange(upper_bound)
    return x_accel, y_accel, z_accel, x_gyro, y_gyro, z_gyro

def get_current_values():
    if DEBUG:
        return mock()
    else:
        raise Exception("get_current_values not implemented!")

def analyze(values: list):
    x_accel = values[0]
    y_accel = values[1]
    z_accel = values[2]
    x_gyro = values[3]
    y_gyro = values[4]
    z_gyro = values[5]
    return FallDetector.determine_if_fall(x_accel, y_accel, z_accel, x_gyro, y_gyro, z_gyro)

def main():
    if DEBUG:
        set_environment_variables()
        
    while True:
        sleep(1)
        values = get_current_values()
        is_fall = analyze(values)
        
        if is_fall:
            print('\n*** ALERT: THIS IS A FALL! ***', values)
            print('*** SENDING AN EMERGENCY ALERT! ***')
            EmergencyAlert.sendEmergencyAlert()
            print('*** EMERGENCY ALERT SENT! ***\n')
            return
        else:
            print('Not a Fall')  

if __name__ == '__main__':
    main()
    