# tests using pytest
# run tests with $ pytest (in the 21122021 directory)

from collatz import collatz_func


class TestClass:
    def test_one(self) -> None:
        numbers = [10, 15]
        output = collatz_func(numbers[0], numbers[1])
        expected = "a"

        assert output == expected, error_message(numbers, expected, output)

    def test_two(self) -> None:
        numbers = [13, 16]
        output = collatz_func(numbers[0], numbers[1])
        expected = "b"

        assert output == expected, error_message(numbers, expected, output)

    def test_three(self) -> None:
        numbers = [53782, 72534]
        output = collatz_func(numbers[0], numbers[1])
        expected = "b"

        assert output == expected, error_message(numbers, expected, output)

    def test_wrong_input(self) -> None:
        numbers = ["1", "wrong"]
        output = collatz_func(numbers[0], numbers[1])
        expected = "Not valid input"

        assert output == expected, error_message(numbers, expected, output)


def error_message(numbers, expected: str, output: str) -> str:
    error_msg = f"Wrong result on input:\n{numbers}\n"
    error_msg += f"should have been:\n{expected}\n"
    error_msg += f"But got:\n{output}"

    return error_msg
