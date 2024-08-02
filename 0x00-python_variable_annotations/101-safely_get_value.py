#!/usr/bin/env python3
from typing import TypeVar, Dict, Union, Optional, Any, Mapping
"""
This module defines a function that safely retrieves a value from a dictionary,
returning a default value if the key is not found.
"""
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary, returning a default value
    if the key is not found.

    Args:
        dct (Mapping[Any, Any]): The dictionary to retrieve the value from.
        key (Any): The key to retrieve from the dictionary.
        default (Optional[T], optional): The default value to return
        if the key is not found.
            Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
