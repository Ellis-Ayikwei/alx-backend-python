#!/usr/bin/env python3
"""a type-annotated function to_kv that takes a string k and an int OR
float v as arguments and returns a tuple. The first element of the tuple
is the string k. The second element is the square of the int/float v and
should be annotated as a float.
"""
from typing import Tuple, List, Union


def to_kv(key: str, value: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string key and a value that can be an int or a float.
    It returns a tuple where the first element is the key and the
    second element
    is the square of the value.

    :param key: A string key.
    :param value: An int or float value.
    :return: A tuple with the key and the square of the value.
    """
    # Square the value
    squared_value = value ** 2

    # Return a tuple with the key and the squared value
    return (key, squared_value)
