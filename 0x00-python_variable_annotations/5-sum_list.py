#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list input_list of floats as
argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all the numbers in the input list.

    Args:
        input_list (List[float]): The list of numbers to calculate the sum of.

    Returns:
        float: The sum of all the numbers in the list.
    """
    return float(sum(input_list))
