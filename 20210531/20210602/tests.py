# tests using pytest
# run tests with $ pytest tests.py (in 20210602)


from factorials import filter_factorials


class TestGame:
    def test_zeros(self) -> None:
        numbers = [0, 0, 0]
        output = filter_factorials(numbers)
        expected = []

        assert output == expected, error_message(numbers, expected, output)

    def test_case_1(self) -> None:
        numbers = [1, 2, 3, 4, 5, 6, 7]
        output = filter_factorials(numbers)
        expected = [1, 2, 6]

        assert output == expected, error_message(numbers, expected, output)

    def test_case_2(self) -> None:
        numbers = [8, 9, 10]
        output = filter_factorials(numbers)
        expected = []

        assert output == expected, error_message(numbers, expected, output)

    def test_case_3(self) -> None:
        numbers = [1, 4, 120]
        output = filter_factorials(numbers)
        expected = [1, 120]

        assert output == expected, error_message(numbers, expected, output)

    def test_negative(self) -> None:
        numbers = [1, 2, 3, 4, 5, -6, 11]
        output = filter_factorials(numbers)
        expected = [1, 2]

        assert output == expected, error_message(numbers, expected, output)


def error_message(num, expected, output) -> str:
    error_msg = f"Wrong result on input:\n{num}\n"
    error_msg += f"should have been:\n{expected}\n"
    error_msg += f"But got:\n{output}"

    return error_msg
