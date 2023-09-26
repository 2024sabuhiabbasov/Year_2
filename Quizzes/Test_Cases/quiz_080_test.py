import pytest
from Quizzes.Codes.quiz_080 import average


# Define custom test names and messages
@pytest.mark.html
@pytest.mark.parametrize("test_input, expected_output, message", [
    ([1, 2, 3, 4, 5], 3.0, "Testing average with positive integers"),
    ([-1, 2, -3, 4, -5], -0.6, "Testing average with mixed integers"),
    ([0.5, 1.0, 1.5, 2.0, 2.5], 1.5, "Testing average with floats"),
])
def test_average(test_input, expected_output, message):
    avg = average(test_input)
    assert avg.average() == expected_output, f"{message}. Expected: {expected_output}, Got: {avg.average()}"


def test_average_with_zero_length_list():
    # Test the average function with an empty list
    with pytest.raises(ZeroDivisionError, match=r"division by zero"):
        avg = average([])
        avg.average()


def test_average_2_with_zero_length_list():
    # Test the average_2 function with an empty list
    with pytest.raises(ZeroDivisionError, match=r"division by zero"):
        avg = average([])
        avg.average_2()


def test_average_3_with_zero_length_list():
    # Test the average_3 function with an empty list
    with pytest.raises(ZeroDivisionError, match=r"division by zero"):
        avg = average([])
        avg.average_3()


if __name__ == "__main__":
    pytest.main()
