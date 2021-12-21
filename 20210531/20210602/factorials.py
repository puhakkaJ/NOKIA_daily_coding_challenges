"""Created 02.6.2021
Challenge from https://edabit.com/challenge/G9QRtAGXb9Cu368Pw
Factorials

Explanation:
Create a function that filters out factorials from a list."""

import typing
import math


def filter_factorials(numbers: typing.List[int]) -> typing.List[int]:
    factorials = []

    for number in numbers:
        i = 1

        while math.factorial(i) < number:
            i += 1

        if math.factorial(i) == number:
            factorials.append(number)

    return factorials
