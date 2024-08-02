#!/usr/bin/env python3
"""
This module defines a function that safely returns the first element of a sequence
if it exists, otherwise returns None.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
