#!/usr/bin/env python3
""" type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
"""
from typing import List, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given number by a specified factor.

    Args:
        factor (float): The factor by which to multiply the number.

    Returns:
        Callable[[float], float]: A function that takes a number as input
        and returns the product of the number and the factor.
    """
    def multiply(number: float) -> float:
        """
        Multiplies a given number by a specified factor.

        Args:
            number (float): The number to be multiplied.

        Returns:
            float: The product of the number and the factor.
        """
        return number * multiplier

    return multiply
