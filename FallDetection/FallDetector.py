#!/usr/bin/env python3

"""
A Python fall detection algorithm using accelerometer and gyroscope data.
"""

from statistics import mean
import math

from Debug.DEBUG import *
WINDOW_SIZE = 50
WINDOW_SLIDE_OFFSET = 1

__author__ = "ECE 477 Fall 2021 Team 12"
__copyright__ = "Copyright 2021, Brace for Impact"
__credits__ = ["ECE 477 Fall 2021 Team 12"]
__version__ = "0.1.0"
__maintainer__ = "Charles Pisciotta"
__email__ = "cpisciot@purdue.edu"
__status__ = "Development"
__date__ = "October 12, 2021"

##############################
# CONSTANTS
##############################

THRESHOLD_3D_ACCEL = 1000  # Used with acceleration data on xyz


##############################
# HELPER FUNCTIONS
##############################

def determine_smallest_dimension_length(values: list) -> int:
    # There should be 3 elements in `values`: x_forces, y_forces, and z_forces
    # Get the length of each dimension to ensure that the minimum length is used for processing
    #   - This avoids an index out of bounds error
    assert  len(values) == 3
    x_dim_len = values[0]
    y_dim_len = values[1]
    z_dim_len = values[2]

    # Get the length of the dimension with the smallest length
    # Using the minimum value avoids index out of range errors
    minimum_length = min([x_dim_len, y_dim_len, z_dim_len])

    # For debugging purposes, check that each dimension has the same length
    #   - Each dimension should be the same length because x, y, and z are collected at the same time
    # When lists are of equal length, the minimum length and the maximum length should be equal
    maximum_length = max([x_dim_len, y_dim_len, z_dim_len])
    assert minimum_length == maximum_length

    return minimum_length


def transform_entries(values: list, length: int) -> list:
    """
    The values are received in the following manner:

    values = [
      [ x1 , x2 , x3 , x4 , ... , xa ],   * where a is x_dim_len
      [ y1 , y2 , y3 , y4 , ... , yb ],   * where b is y_dim_len
      [ z1 , z2 , z3 , z4 , ... , zc ],   * where c is z_dim_len
    ]


    Transform the values to the following structure for fall detection analysis:

    transformed_values = [
      [ x1 , y1 , z1 ],
      [ x2 , y2 , z2 ],
      [ x3 , y3 , z3 ],
      [ .. , .. , .. ],
      [ xn , yn , zn ],   * where n is `length`
    ]
    """
    return list(zip(*values[:length]))


def get_3d_magnitude(dimension_values: list) -> float:
    """
    This function gets the 3-d magnitude of x, y, and z values

    Parameters:
      - dimension_values: list

        dimension_values = [ x_value , y_value , z_value ]
          - x_value: The force experienced in the x-dimension
          - y_value: The force experienced in the y-dimension
          - z_value: The force experienced in the z-dimension

    Returns:
      - f_value: The 3-dimensional force calculated with the 3D magnitude formula

    3D Magnitude Formula:
      Force = √ (x**2) + (y**2) + (z**2)
    """

    # There should be 3 dimension values: x, y, and z
    assert len(dimension_values) == 3

    x_squared = dimension_values[0] ** 2
    y_squared = dimension_values[1] ** 2
    z_squared = dimension_values[2] ** 2
    return math.sqrt(x_squared + y_squared + z_squared)


def map_1d_values_to_3d_values(individual_values) -> list:
    """
    Map the list from individual force values to 3-dimensional force values

    Currently, the list contains the individual x, y, and z forces experienced by the sensor as follows:

        individual_values = [
          [ x1 , y1 , z1 ],
          [ x2 , y2 , z2 ],
          [ x3 , y3 , z3 ],
          [ .. , .. , .. ],
          [ xn , yn , zn ]
        ]

    Use a mapping function to convert each entry from individual dimensions to 3-dimensional values:

        mappedForceValues = [ f1 , f2 , f3 , f4 , f5 , ... , fn ]
    """
    return list(map(get_3d_magnitude, individual_values))


def window_generator(values: list, window_size: int, slide_offset: int = 1):
    """
    Creates a generator, yielding a slice of the values with a sliding window of length `window_size`

    # Given:
    #   values = [ f1 , f2 , f3 , f4 , f5 , f6 , f7 , f8 , f9 , ... , fn ]
    #   window_size = 5
    #   window_slide = 1
    #
    # Iteration 1:
    #   Yields: [ f1 , f2 , f3 , f4 , f5 ]
    #
    # Iteration 2:
    #   Yields: [ f2 , f3 , f4 , f5 , f6 ]
    #
    # Iteration 3:
    #   Yields: [ f3 , f4 , f5 , f6 , f7 ]
    #
    # ...
    #
    # Iteration n - window_size (Final Iteration):
    #   Yields: [ fn-4 , fn-3 , fn-2 , fn-1 , fn ]

    :param values: The 3-dimensional force values.
    :param window_size: The desired window size for analysis
    :param slide_offset: The desired positive offset from a window start index to the next window start index.
    :return: A generator for each sliding window
    """

    # The number of entries in the values list
    len_values = len(values)

    # Yield
    for start_index in range(0, len_values - window_size, slide_offset):
        yield values[start_index:start_index+window_size]


def log_fall(window):
    average_force = mean(window)
    print(f"A fall is detected with average value: {average_force}")


##############################
# FALL Detection
##############################

def check_window_for_fall(window_values: list) -> bool:
    # TODO: Analyze a window for a fall
    return False


def determine_if_fall(values: list) -> bool:

    # Determine minimum length
    smallest_dim_len = determine_smallest_dimension_length(values)

    # Transform the list from dimension entries to time entries
    transformed_values = transform_entries(values, smallest_dim_len)

    # Map the list from 1-dimensional force value lists to 3-dimensional force values
    mapped_force_values = map_1d_values_to_3d_values(transformed_values)

    # Analyze the force values for each window
    for window in window_generator(mapped_force_values, WINDOW_SIZE, WINDOW_SLIDE_OFFSET):

        # Check for fall in given window
        is_fall_detected = check_window_for_fall(window)

        # Handle a detected fall
        if is_fall_detected:
            log_fall(window)
            return True

    # No fall detected
    return False
