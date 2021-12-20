# tests using pytest
# run tests with $ pytest tests.py

from love import love_game
import typing


class TestGame:
    def test_six(self) -> None:
        num = 6
        output = love_game(num)
        expected = (
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
        )

        assert output == expected, error_message(num, expected, output)

    def test_one(self) -> None:
        num = 1
        output = love_game(num)
        expected = "LOVES ME"

        assert output == expected, error_message(num, expected, output)

    def test_three(self) -> None:
        num = 3
        output = love_game(num)
        expected = "Loves me, Loves me not, LOVES ME"

        assert output == expected, error_message(num, expected, output)

    def test_zero(self) -> None:
        num = 0
        output = love_game(num)
        expected = ""

        assert output == expected, error_message(num, expected, output)

    def test_eight(self) -> None:
        num = 8
        output = love_game(num)
        expected = "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

        assert output == expected, error_message(num, expected, output)


def error_message(num, expected, output) -> str:
    error_msg = f"Wrong result on input:\n{num}\n"
    error_msg += f"should have been:\n{expected}\n"
    error_msg += f"But got:\n{output}"

    return error_msg
