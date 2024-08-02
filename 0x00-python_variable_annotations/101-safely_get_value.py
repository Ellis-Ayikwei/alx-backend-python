#!/usr/bin/env python3
from typing import TypeVar, Union, Optional, Any, Mapping

"""
This module defines a function that safely retrieves a value
from a dictionary,
returning a default value if the key is not found.
"""

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary, returning a default value
    if the key is not found.

    :param dct: A mapping (dictionary) from which to retrieve the value.
    :param key: The key whose value is to be retrieved.
    :param default: The default value to return if the key is not found.
    Default is None.
    :return: The value associated with the key if it exists, otherwise
    the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
