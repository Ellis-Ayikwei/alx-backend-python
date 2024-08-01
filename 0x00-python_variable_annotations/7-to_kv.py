#!/usr/bin/env python3
"""a type-annotated function to_kv that takes a string k and an int OR
float v as arguments and returns a tuple. The first element of the tuple
is the string k. The second element is the square of the int/float v and
should be annotated as a float.
"""

from typing import Tuple, List, Union


def to_kv(key: str, value: Union[int, float]) -> Tuple[str, float]:
    return (key, value ** 2)
