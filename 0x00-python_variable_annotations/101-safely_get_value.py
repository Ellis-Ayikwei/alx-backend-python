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
    """
    if key in dct:
        return dct[key]
    else:
        return default
