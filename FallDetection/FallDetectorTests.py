#!/usr/bin/env python3

"""
A Python fall detection algorithm using accelerometer and gyroscope data.
"""

import unittest
from FallDetection.FallDetector import FallDetector

NON_TRIGGER_HORIZONTAL_ACCEL = 0
TRIGGER_HORIZONTAL_ACCEL = 111

NON_TRIGGER_VERTICAL_ACCEL = 0
TRIGGER_VERTICAL_ACCEL = 111

NON_TRIGGER_HORIZONTAL_GYRO = 0
TRIGGER_HORIZONTAL_GYRO = 111

NON_TRIGGER_VERTICAL_GYRO = 0
TRIGGER_VERTICAL_GYRO = 111

class TestStringMethods(unittest.TestCase):

    def test_example(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
