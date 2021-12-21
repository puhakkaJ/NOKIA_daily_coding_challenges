# Created 21.12.2021
# Challenge from https://edabit.com/challenge/6JNHBeGxY8dhTaPhs
# 3n + 1 Problem (Collatz Conjecture)

# Explanation:
# If even: divide by 2.
# If odd: multiply by 3, then add 1.
# The Collatz algorithm always reaches 1 for all positive integers.

# Create a function that, when given two positive integers a b, returns "a"
# if integer a took fewer steps to reach 1 than b when passed through
# the Collatz sequence, or "b" if integer b took fewer steps to reach 1 than a.


def collatz_func(a: int, b: int) -> str:
    try:
        numbers = [a, b]
        outputs = ["a", "b"]

        while numbers[0] != 1 and numbers[1] != 1:
            for i in range(2):
                if numbers[i] % 2 == 0:
                    numbers[i] /= 2
                else:
                    numbers[i] *= numbers[i] * 3 + 1

        return outputs[numbers.index(1)]
    except TypeError:
        return "Not valid input"
