#!/usr/bin/env python3
from typing import TypeVar, Dict, Union, Optional, Any, Mapping
"""
This module defines a function that safely retrieves a value from a dictionary,
returning a default value if the key is not found.
"""


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary, returning a default value
    if the key is not found.

    :param dct: Dictionary from which to retrieve the value.
    :param key: Key whose value is to be retrieved.
    :param default: Default value to return if the key is not found.
    :return: The value associated with the key if it exists, otherwise
    the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
