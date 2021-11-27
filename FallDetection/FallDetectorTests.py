#!/usr/bin/env python3

"""
A Python fall detection algorithm using accelerometer and gyroscope data.
"""

import unittest
import csv
import os
from FallDetector import FallDetector

NON_TRIGGER_HORIZONTAL_ACCEL = 0
TRIGGER_HORIZONTAL_ACCEL = 111

NON_TRIGGER_VERTICAL_ACCEL = 0
TRIGGER_VERTICAL_ACCEL = 111

NON_TRIGGER_HORIZONTAL_GYRO = 0
TRIGGER_HORIZONTAL_GYRO = 111

NON_TRIGGER_VERTICAL_GYRO = 0
TRIGGER_VERTICAL_GYRO = 111

def fall_filepath(filename):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, f"TestData/Fall/{filename}")

def no_fall_filepath(filename):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, f"TestData/NoFall/{filename}")

def load_test_file(filepath):
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        values = []

        for row in csv_reader:
            
            # Drop lines w/o 3 or 6 values
            # 3 value lines should only be accelerometer
            # 6 value lines should be accelerometer and gyro
            row_len = len(row)

            if (row_len != 3) and (row_len != 6):
                continue

            # Convert all list values from str to the absolute integer value
            row = [abs(int(value)) for value in row]

            # Pad list with 3 trailing 0s if accelerometer only
            if row_len == 3:
                row += [0, 0, 0]

            values.append(row)

        return values

class FallDetectorTests(unittest.TestCase):

    ############################################################
    # FALL DATA
    ############################################################

    ##############################
    # FALL DATA - BRETT
    ##############################

    def test_brett_fall_1(self):
        filepath = fall_filepath('brett_fall_1.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    def test_brett_fall_2(self):
        filepath = fall_filepath('brett_fall_2.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    def test_brett_fall_3(self):
        filepath = fall_filepath('brett_fall_3.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    def test_brett_fall_4(self):
        filepath = fall_filepath('brett_fall_4.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    def test_brett_fall_5(self):
        filepath = fall_filepath('brett_fall_5.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    ##############################
    # FALL DATA - CHARLES
    ##############################

    def test_charles_fall_1(self):
        filepath = fall_filepath('charles_fall_1.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    def test_charles_fall_2(self):
        filepath = fall_filepath('charles_fall_2.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    def test_charles_fall_3(self):
        filepath = fall_filepath('charles_fall_3.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    ##############################
    # FALL DATA - PREM
    ##############################

    def test_prem_fall_1(self):
        filepath = fall_filepath('prem_fall_1.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    def test_prem_fall_2(self):
        filepath = fall_filepath('prem_fall_2.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertTrue(is_fall)

    ############################################################
    # NO FALL DATA
    ############################################################
    
    ##############################
    # NO FALL DATA - PREM
    ##############################

    def test_prem_walk_1(self):
        filepath = no_fall_filepath('prem_walk_1.txt')
        values = load_test_file(filepath)
        is_fall = FallDetector.determine_if_fall(values)
        self.assertFalse(is_fall)


if __name__ == '__main__':
    unittest.main()
