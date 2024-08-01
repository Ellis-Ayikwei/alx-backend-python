#!/usr/bin/env python3
"""function floor which takes a float n as argument and returns the
floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of a float number.

    Args:
        n (float): The float number to take the floor of.

    Returns:
        int: The floor of the float number.
    """
    # Use the math.floor function to round down the float number to the nearest integer.
    # Convert the result to an integer using the int function.
    return int(math.floor(n))
