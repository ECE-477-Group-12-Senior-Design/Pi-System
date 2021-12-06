#!/usr/bin/env python3

"""
A Python fall detection algorithm using accelerometer and gyroscope data.
"""

from statistics import mean
import math

from Debug.DEBUG import *
WINDOW_SIZE = 50

__author__ = "ECE 477 Fall 2021 Team 12"
__copyright__ = "Copyright 2021, Brace for Impact"
__credits__ = ["ECE 477 Fall 2021 Team 12"]
__version__ = "0.1.0"
__maintainer__ = "Charles Pisciotta"
__email__ = "cpisciot@purdue.edu"
__status__ = "Development"
__date__ = "October 12, 2021"


class FallDetector:

    THRESHOLD_1D_ACCEL_HORIZONTAL = 1500  # Used with acceleration data on the x and z axes
    THRESHOLD_1D_ACCEL_VERTICAL = 1500  # Used with acceleration data on the z axis
    THRESHOLD_2D_ACCEL_HORIZONTAL = 1300  # Used with accelertaion data on the xy plane
    THRESHOLD_2D_ACCEL_VERTICAL = 1300  # Used with acceleration data on the xz and yz planes
    THRESHOLD_3D_ACCEL = 1220  # Used with accelearaion data on xyz

    THRESHOLD_1D_GYRO_HORIZONTAL = 157220  # Used with gyroscope data on the x and z axes
    THRESHOLD_1D_GYRO_VERTICAL = 154683  # Used with gyroscope data on the z axis
    THRESHOLD_2D_GYRO_HORIZONTAL = 184989  # Used with gyroscope data on the xy plane
    THRESHOLD_2D_GYRO_VERTICAL = 194315  # Used with gyroscope data on the xz and yz planes
    THRESHOLD_3D_GYRO = 227322  # Used with gyroscope data on xyz

    @staticmethod
    def __logFall(id, value, threshold):
        if MAIN_DEBUG:
            print('{} detected a fall with value={} and threshold={}'.format(id, value, threshold))

    # TODO: Add comment
    @staticmethod
    def determine_if_fall(values: list, expects_fall=True) -> bool:

        for index in range(0, len(values), WINDOW_SIZE):
            columns = list(zip(*values[index:index + WINDOW_SIZE]))

            x_accels = columns[0]
            y_accels = columns[1]
            z_accels = columns[2]

            x_gyros = columns[3]
            y_gyros = columns[4]
            z_gyros = columns[5]

            # DEBUG flag checks if should skip accel checking
            if TEST_CHECK_ACCEL:
                accel_is_fall = FallDetector.__determine_if_fall_accelerometer(x_accels, y_accels, z_accels, expects_fall)

                # Optimization: Can return True early if we know accel has detected a fall
                if accel_is_fall:
                    return True

            # This will skip gyro checking while debugging
            if not TEST_CHECK_GYRO:
                continue

            gyro_is_fall = FallDetector.__determine_if_fall_gyroscope(x_gyros, y_gyros, z_gyros, expects_fall)

            if gyro_is_fall:
                return True
        
        return False

    '''
    Description: Given accelerometer sensor data, determine if the data is consistent with a fall.
    Parameters: x, y, and z values for the accelerometer at a given time instant.
    Returns: A Boolean. If a fall, returns True. If not a fall, returns False.
    '''
    @staticmethod
    def __determine_if_fall_accelerometer(x_accels, y_accels, z_accels, expects_fall=True) -> bool:
        
        if mean(x_accels) > FallDetector.THRESHOLD_1D_ACCEL_HORIZONTAL:
            if not expects_fall:
                FallDetector.__logFall('A1 THRESHOLD_1D_ACCEL_HORIZONTAL', mean(x_accels), FallDetector.THRESHOLD_1D_ACCEL_HORIZONTAL)
            return True
        elif mean(y_accels) > FallDetector.THRESHOLD_1D_ACCEL_HORIZONTAL:
            if not expects_fall:
                FallDetector.__logFall('A2 THRESHOLD_1D_ACCEL_HORIZONTAL', mean(y_accels), FallDetector.THRESHOLD_1D_ACCEL_HORIZONTAL)
            return True
        elif mean(z_accels) > FallDetector.THRESHOLD_1D_ACCEL_VERTICAL:
            if not expects_fall:
                FallDetector.__logFall('A3 THRESHOLD_1D_ACCEL_VERTICAL', mean(z_accels), FallDetector.THRESHOLD_1D_ACCEL_VERTICAL)
            return True
        elif FallDetector.__get_2d_magnitude_average(x_accels, y_accels) > FallDetector.THRESHOLD_2D_ACCEL_HORIZONTAL:
            if not expects_fall:
                FallDetector.__logFall('A4 THRESHOLD_2D_ACCEL_HORIZONTAL', FallDetector.__get_2d_magnitude_average(x_accels, y_accels), FallDetector.THRESHOLD_2D_ACCEL_HORIZONTAL)
            return True
        elif FallDetector.__get_2d_magnitude_average(x_accels, z_accels) > FallDetector.THRESHOLD_2D_ACCEL_VERTICAL:
            if not expects_fall:
                FallDetector.__logFall('A5 THRESHOLD_2D_ACCEL_VERTICAL', FallDetector.__get_2d_magnitude_average(x_accels, z_accels), FallDetector.THRESHOLD_2D_ACCEL_VERTICAL)
            return True
        elif FallDetector.__get_2d_magnitude_average(y_accels, z_accels) > FallDetector.THRESHOLD_2D_ACCEL_VERTICAL:
            if not expects_fall:
                FallDetector.__logFall('A6 THRESHOLD_2D_ACCEL_VERTICAL', FallDetector.__get_2d_magnitude_average(y_accels, z_accels), FallDetector.THRESHOLD_2D_ACCEL_VERTICAL)
            return True
        elif FallDetector.__get_3d_magnitude_average(x_accels, y_accels, z_accels) > FallDetector.THRESHOLD_3D_ACCEL:
            if not expects_fall:
                FallDetector.__logFall('A7 THRESHOLD_3D_ACCEL', FallDetector.__get_3d_magnitude_average(x_accels, y_accels, z_accels), FallDetector.THRESHOLD_3D_ACCEL)
            return True

        return False

    # TODO: Add doc comment
    @staticmethod
    def __determine_if_fall_gyroscope(x_gyros, y_gyros, z_gyros, expects_fall=True) -> bool:
        if mean(x_gyros) > FallDetector.THRESHOLD_1D_GYRO_HORIZONTAL:
            if not expects_fall:
                FallDetector.__logFall('G1 THRESHOLD_1D_GYRO_HORIZONTAL', mean(x_gyros), FallDetector.THRESHOLD_1D_GYRO_HORIZONTAL)
            return True
        elif mean(y_gyros) > FallDetector.THRESHOLD_1D_GYRO_HORIZONTAL:
            if not expects_fall:
                FallDetector.__logFall('G2 THRESHOLD_1D_GYRO_HORIZONTAL', mean(y_gyros), FallDetector.THRESHOLD_1D_GYRO_HORIZONTAL)
            return True
        elif mean(z_gyros) > FallDetector.THRESHOLD_1D_GYRO_VERTICAL:
            if not expects_fall:
                FallDetector.__logFall('G3 THRESHOLD_1D_GYRO_VERTICAL', mean(z_gyros), FallDetector.THRESHOLD_1D_GYRO_VERTICAL)
            return True
        elif FallDetector.__get_2d_magnitude_average(x_gyros, y_gyros) > FallDetector.THRESHOLD_2D_GYRO_HORIZONTAL:
            if not expects_fall:
                FallDetector.__logFall('G4 THRESHOLD_2D_GYRO_HORIZONTAL', FallDetector.__get_2d_magnitude_average(x_gyros, y_gyros), FallDetector.THRESHOLD_2D_GYRO_HORIZONTAL)
            return True
        elif FallDetector.__get_2d_magnitude_average(x_gyros, z_gyros) > FallDetector.THRESHOLD_2D_GYRO_VERTICAL:
            if not expects_fall:
                FallDetector.__logFall('G5 THRESHOLD_2D_GYRO_VERTICAL', FallDetector.__get_2d_magnitude_average(x_gyros, z_gyros), FallDetector.THRESHOLD_2D_GYRO_VERTICAL)
            return True
        elif FallDetector.__get_2d_magnitude_average(y_gyros, z_gyros) > FallDetector.THRESHOLD_2D_GYRO_VERTICAL:
            if not expects_fall:
                FallDetector.__logFall('G6 THRESHOLD_2D_GYRO_VERTICAL', FallDetector.__get_2d_magnitude_average(y_gyros, z_gyros), FallDetector.THRESHOLD_2D_GYRO_VERTICAL)
            return True
        elif FallDetector.__get_3d_magnitude_average(x_gyros, y_gyros, z_gyros) > FallDetector.THRESHOLD_3D_GYRO:
            if not expects_fall:
                FallDetector.__logFall('G7 THRESHOLD_3D_GYRO', FallDetector.__get_3d_magnitude_average(x_gyros, y_gyros, z_gyros), FallDetector.THRESHOLD_3D_GYRO)
            return True

        return False

    @staticmethod
    def __get_2d_magnitude_average(first, second):
        first = list(map(lambda x: x ** 2, first))
        second = list(map(lambda x: x ** 2, second))
        magnitudes = [math.sqrt(first[i] + second[i]) for i in range(len(min(first, second)))]
        return mean(magnitudes)

    @staticmethod
    def __get_3d_magnitude_average(first, second, third):
        first = list(map(lambda x: x ** 2, first))
        second = list(map(lambda x: x ** 2, second))
        third = list(map(lambda x: x ** 2, third))
        magnitudes = [math.sqrt(first[i] + second[i] + third[i]) for i in range(len(min(first, second, third)))]
        return mean(magnitudes)