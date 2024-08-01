#!/usr/bin/env python3
"""function concat that takes a string str1 and a string
str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string to be concatenated.
        str2 (str): The second string to be concatenated.

    Returns:
        str: The concatenated string.
    """
    # Concatenate the two input strings
    # Convert the concatenated result to string type
    return str(str1 + str2)
