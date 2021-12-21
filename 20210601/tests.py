# tests using pytest
# run tests with $ pytest tests.py in 20210601

from consecutive import consecutive_combo


class TestFunction:
    # Testing with only zeros. Should return True.
    def test_only_zeros(self) -> None:
        output = consecutive_combo([0, 0], [0])
        expected = True

        assert output == expected, error_message(expected, output)

    # Testing with wrong input type.
    def test_wrong_input(self) -> None:
        output = consecutive_combo("wrong", [2, 3, 6])
        expected = False
        print(output)

        assert output == expected, error_message(expected, output)

    def test_case_1(self) -> None:
        output = consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9])
        expected = False

        assert output == expected, error_message(expected, output)

    def test_case_2(self) -> None:
        output = consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])
        expected = False

        assert output == expected, error_message(expected, output)

    # Testing with duplicates. Duplicates should not affect to the result.
    def test_duplicates(self) -> None:
        output = consecutive_combo([44, 45, 45], [43])
        expected = True

        assert output == expected, error_message(expected, output)


def error_message(expected, output) -> str:
    error_msg = f"should have been:\n{expected}\n"
    error_msg += f"But got:\n{output}"

    return error_msg
