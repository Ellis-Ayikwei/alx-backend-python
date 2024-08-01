#!/usr/bin/env python3


from typing import List, Tuple, Sequence, Iterable
"""
This module defines a function that takes an iterable of sequences and returns
a list of tuples. Each tuple contains a sequence from the input iterable and
its length.

The function, `element_length`, takes an iterable of sequences as input and
returns a list of tuples. Each tuple contains a sequence from the input
iterable and its length.

Args:
    lst (Iterable[Sequence]): An iterable of sequences.

Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a
    sequence from the input iterable and its length.
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes an iterable of sequences and returns a list of tuples.
    Each tuple contains a sequence from the input iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a
        sequence from the input iterable and its length.
    """

    # List comprehension to iterate over the input iterable of sequences
    # and for each sequence, create a tuple containing the sequence and its length.
    return [(seq, len(seq)) for seq in lst]
