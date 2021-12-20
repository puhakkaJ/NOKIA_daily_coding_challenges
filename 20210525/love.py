"""Created 25.5.2021
Challenge from https://edabit.com/challenge/6pEGXsuCAxbWTRkgc
Loves Me, Loves Me Not...

Explanation:
"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, 
saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, 
loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" 
for every alternating petal, and return the last phrase in all caps. 
Remember to put a comma and space between phrases."""


def loves_me(i: int, num: int) -> str:
    love_yes = "Loves me"

    if i == num - 1:
        return love_yes.upper()

    return love_yes


def loves_me_not(i: int, num: int) -> str:
    love_no = " not"

    if i == num - 1:
        return love_no.upper()

    return love_no


def love_game(num: int) -> str:
    result = ""

    for i in range(num):
        result += str(loves_me(i, num))

        if i % 2 != 0:
            result += str(loves_me_not(i, num))
        result += ", "

    return result[:-2]
