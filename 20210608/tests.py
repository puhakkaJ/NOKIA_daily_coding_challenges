from hypothesis import given, strategies as st
from pandigital import is_pandigital, find_pandigital_products


# Testing with hypothesis lib. Generates random x, y > 0 values.
@given(x=st.integers(min_value=0), y=st.integers(min_value=0))
def test_random(x, y) -> None:
    output = is_pandigital(x, y)
    multiplication = str(x) + "*" + str(y) + "=" + str(x * y)

    if multiplication in find_pandigital_products():
        expected = True
    else:
        expected = False

    assert output == expected, error_message(expected, output)


def test_right_case() -> None:
    x = 4
    y = 1963

    output = is_pandigital(x, y)
    multiplication = str(x) + "*" + str(y) + "=" + str(x * y)

    if multiplication in find_pandigital_products():
        expected = True
    else:
        expected = False

    print(multiplication, output)

    assert output == expected, error_message(expected, output)


def error_message(expected, output) -> str:
    error_msg = f"should have been:\n{expected}\n"
    error_msg += f"But got:\n{output}"

    return error_msg


if __name__ == "__main__":
    test_random()
    test_right_case()
    print("Success. All passed!")  # if no errors
