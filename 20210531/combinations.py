"""Created 31.5.2021
Challenge from https://edabit.com/challenge/G9QRtAGXb9Cu368Pw
Combinations

Explanation:
Create a function that takes a variable number of arguments,
each argument representing the number of items in a group,
and returns the number of permutations (combinations) of items
that you could get by taking one item from each group."""


def non_zero(num: int) -> bool:
    if num != 0:
        return True
    else:
        return False


def combinations(*elements: int) -> int:
    numbers = list(filter(non_zero, elements))

    try:
        comb = numbers[0]

        for number in numbers[1:]:
            comb *= number
        return comb

    except IndexError:
        return 0
