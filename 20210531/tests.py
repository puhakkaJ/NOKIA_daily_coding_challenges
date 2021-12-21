# tests using pytest
# run tests with $ pytest tests.py

from combinations import combinations


class TestFunction:
    def test_only_zeros(self) -> None:
        output = combinations(0, 0)
        expected = 0

        assert output == expected, error_message(expected, output)

    def test_case_1(self) -> None:
        output = combinations(2, 3)
        expected = 6

        assert output == expected, error_message(expected, output)

    def test_case_2(self) -> None:
        output = combinations(3, 7, 4)
        expected = 84

        assert output == expected, error_message(expected, output)

    def test_case_3(self) -> None:
        output = combinations(2, 3, 4, 5)
        expected = 120

        assert output == expected, error_message(expected, output)

    def test_case_4(self) -> None:
        output = combinations(2, 5, 0, 8, 0)
        expected = 80

        assert output == expected, error_message(expected, output)


def error_message(expected, output) -> str:
    error_msg = f"should have been:\n{expected}\n"
    error_msg += f"But got:\n{output}"

    return error_msg
