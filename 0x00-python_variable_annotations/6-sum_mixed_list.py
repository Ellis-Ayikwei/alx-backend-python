#!/usr/bin/env python3
"""a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mixed_list (List[Union[int, float]]): List of
        mixed integers and floats.

    Returns:
        float: The sum of the mixed list.
    """
    return sum(mixed_list)
