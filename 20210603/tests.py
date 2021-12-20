import sys
from hypothesis import given, strategies as st
from shift import shift_left


# Testing with hypothesis lib. Generates random x, y values.
@given(x=st.integers(), y=st.integers(min_value=0, max_value=1000))
def test_cases(x, y) -> None:
    output = shift_left(x, y)
    expected = x * pow(2, y)

    assert output == expected, error_message(expected, output)


def error_message(expected, output) -> str:
    error_msg = f"should have been:\n{expected}\n"
    error_msg += f"But got:\n{output}"

    return error_msg


if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    test_cases()
    print("Success. All passed!")  # if no errors
