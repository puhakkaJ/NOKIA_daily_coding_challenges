"""Created 28.5.2021
Challenge from https://edabit.com/challenge/E882au3CJba2jfQyT
Finding Common Elements

Explanation:
Create a function that takes two lists of numbers sorted in ascending order
and returns a list of numbers which are common to both the input lists."""

import typing


def common_elements(elements_1: typing.List[int], elements_2: typing.List[int]) -> int:
    elements_2_set = set(elements_2)
    elements_1_set = set(elements_1)

    return sorted(elements_1_set & elements_2_set)
