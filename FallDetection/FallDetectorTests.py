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

    def test_not_a_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertFalse(isFall, 'Did not expect fall')

    def test_trigger_x_accel_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')
    
    def test_trigger_y_accel_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')
    
    def test_trigger_z_accel_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')
    
    def test_trigger_x_gyro_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')
    
    def test_trigger_y_gyro_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')
    
    def test_trigger_z_gyro_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')
    
    def test_trigger_x_y_accel_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')
    
    def test_trigger_x_z_accel_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')

    def test_trigger_y_z_accel_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')

    def test_trigger_x_y_gyro_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')

    def test_trigger_x_z_gyro_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')

    def test_trigger_y_z_gyro_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')

    def test_trigger_x_y_z_accel_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=TRIGGER_HORIZONTAL_ACCEL, 
                                                y_accel=TRIGGER_HORIZONTAL_ACCEL, 
                                                z_accel=TRIGGER_VERTICAL_ACCEL, 
                                                x_gryo=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                y_gyro=NON_TRIGGER_HORIZONTAL_GYRO, 
                                                z_gyro=NON_TRIGGER_VERTICAL_GYRO)
        
        self.assertTrue(isFall, 'Expected not a fall')

    def test_trigger_x_y_z_gyro_fall(self):
        isFall = FallDetector.determine_if_fall(x_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                            y_accel=NON_TRIGGER_HORIZONTAL_ACCEL, 
                                            z_accel=NON_TRIGGER_VERTICAL_ACCEL, 
                                            x_gryo=TRIGGER_HORIZONTAL_GYRO, 
                                            y_gyro=TRIGGER_HORIZONTAL_GYRO, 
                                            z_gyro=TRIGGER_VERTICAL_GYRO)
    
        self.assertTrue(isFall, 'Expected not a fall')

if __name__ == '__main__':
    unittest.main()
