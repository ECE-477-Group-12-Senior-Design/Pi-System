#!/usr/bin/env python3

"""
A Python fall detection algorithm using accelerometer and gyroscope data.
"""

from statistics import mean
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

    # TODO: Add comment
    @staticmethod
    def determine_if_fall(values) -> bool:
        columns = list(zip(*values))
        x_accels = columns[0]
        y_accels = columns[1]
        z_accels = columns[2]

        x_gyros = columns[3]
        y_gyros = columns[4]
        z_gyros = columns[5]

        accel_is_fall = FallDetector.__determine_if_fall_accelerometer(x_accels, y_accels, z_accels)

        # Optimization: Can return True early if we know accel has detected a fall
        if accel_is_fall:
            return True

        return FallDetector.__determine_if_fall_gyroscope(x_gyros, y_gyros, z_gyros)

    '''
    Description: Given accelerometer sensor data, determine if the data is consistent with a fall.
    Parameters: x, y, and z values for the accelerometer at a given time instant.
    Returns: A Boolean. If a fall, returns True. If not a fall, returns False.
    '''
    @staticmethod
    def __determine_if_fall_accelerometer(x_accels, y_accels, z_accels) -> bool:
        
        if mean(x_accels) > FallDetector.THRESHOLD_1D_ACCEL_HORIZONTAL:
            return True
        elif mean(y_accels) > FallDetector.THRESHOLD_1D_ACCEL_HORIZONTAL:
            return True
        elif mean(z_accels) > FallDetector.THRESHOLD_1D_ACCEL_VERTICAL:
            return True
        elif FallDetector.__get_2d_magnitude_average(x_accels, y_accels) > FallDetector.THRESHOLD_2D_ACCEL_HORIZONTAL:
            return True
        elif FallDetector.__get_2d_magnitude_average(x_accels, z_accels) > FallDetector.THRESHOLD_2D_ACCEL_VERTICAL:
            return True
        elif FallDetector.__get_2d_magnitude_average(y_accels, z_accels) > FallDetector.THRESHOLD_2D_ACCEL_VERTICAL:
            return True
        elif FallDetector.__get_3d_magnitude_average(x_accels, y_accels, z_accels) > FallDetector.THRESHOLD_3D_ACCEL:
            return True

        return False

    # TODO: Add doc comment
    @staticmethod
    def __determine_if_fall_gyroscope(x_gyros, y_gyros, z_gyros) -> bool:
        if mean(x_gyros) > FallDetector.THRESHOLD_1D_GYRO_HORIZONTAL:
            return True
        elif mean(y_gyros) > FallDetector.THRESHOLD_1D_GYRO_HORIZONTAL:
            return True
        elif mean(z_gyros) > FallDetector.THRESHOLD_1D_GYRO_VERTICAL:
            return True
        elif FallDetector.__get_2d_magnitude_average(x_gyros, y_gyros) > FallDetector.THRESHOLD_2D_GYRO_HORIZONTAL:
            return True
        elif FallDetector.__get_2d_magnitude_average(x_gyros, z_gyros) > FallDetector.THRESHOLD_2D_GYRO_VERTICAL:
            return True
        elif FallDetector.__get_2d_magnitude_average(y_gyros, z_gyros) > FallDetector.THRESHOLD_2D_GYRO_VERTICAL:
            return True
        elif FallDetector.__get_3d_magnitude_average(x_gyros, y_gyros, z_gyros) > FallDetector.THRESHOLD_3D_GYRO:
            return True

        return False

    @staticmethod
    def __get_2d_magnitude_average(first, second):
        first = map(lambda x: x ** 2, first)
        second = map(lambda x: x ** 2, second)
        magnitudes = [math.sqrt(first[i]**2 + second[i]**2) for i in range(len(min(first, second)))]
        return mean(magnitudes)

    @staticmethod
    def __get_3d_magnitude_average(first, second, third):
        first = map(lambda x: x ** 2, first)
        second = map(lambda x: x ** 2, second)
        third = map(lambda x: x ** 2, third)
        magnitudes = [math.sqrt(first[i]**2 + second[i]**2 + third[i]**2) for i in range(len(min(first, second, third)))]
        return mean(magnitudes)