#!/usr/bin/env python3
"""
This module defines a function that zooms in on an input list or tuple.
"""
from typing import Tuple, List, Union


def zoom_array(lst: Union[Tuple, List], factor: int = 2) -> Union[Tuple, List]:
    """
    Zooms in on a list or tuple.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
