"""Created 03.6.2021
Challenge from https://edabit.com/challenge/7soAnzpZToSxztnDr
Recursion: Shift Left by Addition

Explanation:
The shift left operation is similar to multiplication by powers of two.
This can also be achieved with repetitive addition, thus, the process can be done recursively.
Create a recursive function that mimics the shift left operator
and returns the result from the two given integers."""


def shift_left(number: int, power: int) -> int:
    if power == 0:
        return number
    else:
        return 2 * shift_left(number, power - 1)
