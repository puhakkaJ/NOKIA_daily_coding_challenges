"""Created 01.6.2021
Challenge from https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb
Combined Consecutive Sequence

Explanation:
Write a function that returns True if two arrays, when combined,
form a consecutive sequence. A consecutive sequence is a sequence
without any gaps in the integers,
e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not."""


import typing
from itertools import chain


def consecutive_combo(
    elements_1: typing.List[int], elements_2: typing.List[int]
) -> bool:
    try:
        elements_2[len(elements_2) :] = elements_1  # merging lists into one
        all_elements = sorted(set(elements_2))
        current = all_elements[0]

        for element in all_elements[1::]:
            if element != current + 1:
                return False
            current = element

        return True
    except TypeError:
        return False
