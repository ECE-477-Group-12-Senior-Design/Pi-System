#!/usr/bin/env python3

"""
A Python fall detection algorithm using accelerometer and gyroscope data.
"""

import math

__author__ = "ECE 477 Fall 2021 Team 12"
__copyright__ = "Copyright 2021, Brace for Impact"
__credits__ = ["ECE 477 Fall 2021 Team 12"]
__version__ = "0.1.0"
__maintainer__ = "Charles Pisciotta"
__email__ = "cpisciot@purdue.edu"
__status__ = "Development"
__date__ = "October 12, 2021"


class FallDetector:

    THRESHOLD_1D_ACCEL_HORIZONTAL = 100  # Used with acceleration data on the x and z axes
    THRESHOLD_1D_ACCEL_VERTICAL = 100  # Used with acceleration data on the z axis
    THRESHOLD_2D_ACCEL_HORIZONTAL = 100  # Used with accelertaion data on the xy plane
    THRESHOLD_2D_ACCEL_VERTICAL = 100  # Used with acceleration data on the xz and yz planes
    THRESHOLD_3D_ACCEL = 100  # Used with accelearaion data on xyz

    THRESHOLD_1D_GYRO_HORIZONTAL = 100  # Used with gyroscope data on the x and z axes
    THRESHOLD_1D_GYRO_VERTICAL = 100  # Used with gyroscope data on the z axis
    THRESHOLD_2D_GYRO_HORIZONTAL = 100  # Used with gyroscope data on the xy plane
    THRESHOLD_2D_GYRO_VERTICAL = 100  # Used with gyroscope data on the xz and yz planes
    THRESHOLD_3D_GYRO = 100  # Used with gyroscope data on xyz

    '''
    Description: Given accelerometer and gyroscope sensor data, determine if the data is consistent with a fall.
    Parameters: x, y, and z values for the accelerometer and gyroscope at a given time instant.
    Returns: A Boolean. If a fall, returns True. If not a fall, returns False.
    '''
    @staticmethod
    def determine_if_fall(x_accel: int, y_accel: int, z_accel: int, x_gryo: int, y_gyro: int, z_gyro: int) -> bool:
        accel_is_fall = FallDetector.__determine_if_fall_accelerometer(x_accel, y_accel, z_accel)

        # Optimization: Can return True early if we know accel has detected a fall
        if accel_is_fall:
            return True

        return FallDetector.__determine_if_fall_gyroscope(x_gryo, y_gyro, z_gyro)

    '''
    Description: Given accelerometer sensor data, determine if the data is consistent with a fall.
    Parameters: x, y, and z values for the accelerometer at a given time instant.
    Returns: A Boolean. If a fall, returns True. If not a fall, returns False.
    '''
    @staticmethod
    def __determine_if_fall_accelerometer(x_accel: int, y_accel: int, z_accel: int) -> bool:
        if x_accel > FallDetector.THRESHOLD_1D_ACCEL_HORIZONTAL:
            return True
        elif y_accel > FallDetector.THRESHOLD_1D_ACCEL_HORIZONTAL:
            return True
        elif z_accel > FallDetector.THRESHOLD_1D_ACCEL_VERTICAL:
            return True
        elif FallDetector.__get__magnitude(x_accel, y_accel) > FallDetector.THRESHOLD_2D_ACCEL_HORIZONTAL:
            return True
        elif FallDetector.__get__magnitude(x_accel, z_accel) > FallDetector.THRESHOLD_2D_ACCEL_VERTICAL:
            return True
        elif FallDetector.__get__magnitude(y_accel, z_accel) > FallDetector.THRESHOLD_2D_ACCEL_VERTICAL:
            return True
        elif FallDetector.__get__magnitude(x_accel, y_accel, z_accel) > FallDetector.THRESHOLD_3D_ACCEL:
            return True

        return False

    '''
    Description: Given gyroscope sensor data, determine if the data is consistent with a fall.
    Parameters: x, y, and z values for the gyroscope at a given time instant.
    Returns: A Boolean. If a fall, returns True. If not a fall, returns False.
    '''
    @staticmethod
    def __determine_if_fall_gyroscope(x_gyro: int, y_gyro: int, z_gyro: int) -> bool:
        if x_gyro > FallDetector.THRESHOLD_1D_GYRO_HORIZONTAL:
            return True
        elif y_gyro > FallDetector.THRESHOLD_1D_GYRO_HORIZONTAL:
            return True
        elif z_gyro > FallDetector.THRESHOLD_1D_GYRO_VERTICAL:
            return True
        elif FallDetector.__get__magnitude(x_gyro, y_gyro) > FallDetector.THRESHOLD_2D_GYRO_HORIZONTAL:
            return True
        elif FallDetector.__get__magnitude(x_gyro, z_gyro) > FallDetector.THRESHOLD_2D_GYRO_VERTICAL:
            return True
        elif FallDetector.__get__magnitude(y_gyro, z_gyro) > FallDetector.THRESHOLD_2D_GYRO_VERTICAL:
            return True
        elif FallDetector.__get__magnitude(x_gyro, y_gyro, z_gyro) > FallDetector.THRESHOLD_3D_GYRO:
            return True

        return False

    '''
    Description: Given one or more dimensions, determine the magnitude.
    Parameters: One or more dimension magnitudes.
    Returns: The magnitude of the combined dimensions.
    '''
    @staticmethod
    def __get__magnitude(*axes):
        axes = map(lambda x: x ** 2, axes)
        return math.sqrt(sum(axes))
