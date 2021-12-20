# tests using pytest
# run tests with $ pytest tests.py

from commons import common_elements


class TestFunction:
    # Testing with empty list
    def test_empty_list(self) -> None:
        elements_1 = [1, 4, 6, 7]
        elements_2 = []
        output = common_elements(elements_1, elements_2)
        expected = []

        assert output == expected, error_message(expected, output)

    def test_1(self) -> None:
        elements_1 = [1, 10, 6, 7, 3]
        elements_2 = [78, 9, 7, 10, 2, 3]
        output = common_elements(elements_1, elements_2)
        expected = [3, 7, 10]

        assert output == expected, error_message(expected, output)

    # Testing with duplicates
    def test_2(self) -> None:
        elements_1 = [1, 1, 1, 1]
        elements_2 = [6, 3, 8, 1]
        output = common_elements(elements_1, elements_2)
        expected = [1]

        assert output == expected, error_message(expected, output)

    # Testing invalid imput
    def test_3(self) -> None:
        elements_1 = [45, 4, "invalid", 5, 9]
        elements_2 = [9, 1, 44, 34, 5]
        output = common_elements(elements_1, elements_2)
        expected = [5, 9]

        assert output == expected, error_message(expected, output)

    def test_4(self) -> None:
        elements_1 = [1, 2, 3, 4, 5]
        elements_2 = [10, 12, 13, 15]
        output = common_elements(elements_1, elements_2)
        expected = []

        assert output == expected, error_message(expected, output)


def error_message(expected, output) -> str:
    error_msg = f"should have been:\n{expected}\n"
    error_msg += f"But got:\n{output}"

    return error_msg
