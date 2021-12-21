"""Created 08.6.2021
Challenge from https://projecteuler.net/problem=32
Pandigital products

Explanation:
n-digit number is pandigital if it makes use of all the digits 1 to n exactly once
; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

CHANGES: Testing is_pandigital() function with inputs from test.py and checking if it works right with help of the find_pandigital_products()
+++ intentionally leaving the duplicant multiplication results in the pandigitals return list due testing."""


import typing


def is_pandigital(multiplier: int, multiplicand: int) -> bool:
    try:
        product = str(multiplier) + str(multiplicand) + str(multiplier * multiplicand)

        if len(product) != 9:
            return False

        sorted_product = "".join(sorted(product))

        if sorted_product == "123456789":
            return True
        else:
            return False

    except TypeError:
        return False


def find_pandigital_products() -> typing.List[str]:
    pandigitals = []

    for i in range(2, 99):
        j = 1

        while i * j < 9999:
            if is_pandigital(i, j):
                pandigitals.append(str(i) + "*" + str(j) + "=" + str(i * j))
            j += 1

    return pandigitals
