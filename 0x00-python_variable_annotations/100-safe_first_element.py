#!/usr/bin/env pyhton3
"""
This module defines a function that safely returns the first element of a
sequence or None if the sequence is empty.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    :param sequence: A sequence of elements.
    :return: The first element of the sequence if it exists, otherwise None.
    """
    return lst[0] if lst else None
