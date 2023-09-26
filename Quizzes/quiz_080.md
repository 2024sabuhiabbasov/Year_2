# Quiz 080

<img width="max" alt="Screenshot 2023-09-26 at 16 15 10" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/b0385849-0acb-4d75-81f2-11f0607d7321">

## Solution
<img width="max" alt="Screenshot 2023-09-26 at 16 15 10" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/ba7342ea-82da-4f54-9c6b-3adf3c0949d7">

```.py
import random


class average:
    def __init__(self, a: list):
        # Constructor to initialize an instance of the class with a list 'a' as its attribute
        self.a = a

    def sum(self):
        sum = 0
        for i in range(len(self.a)):
            sum += self.a[i]  # Add the current element 'a[i]' to the sum
        return sum  # Return the sum of elements in the list

    def average(self):
        l = len(self.a)  # Get the length of the list 'a'
        return self.sum() / l  # Calculate and return the average by dividing the sum by the length

    def average_2(self):
        i = 0
        l = len(self.a)  # Get the length of the list 'a'
        sum = 0
        while i < l:
            sum += self.a[i]  # Add the current element 'a[i]' to the sum
            i += 1  # Increment the loop counter
        return sum / l  # Calculate and return the average using a while loop

    def average_3(self):
        sum = 0
        for i in range(len(self.a)):
            # Generate a random integer 'k' between the minimum and maximum values in 'a'
            k = random.randint(min(self.a), max(self.a))
            while k != self.a[i]:
                # Keep generating 'k' until it matches the current element 'a[i]'
                k = random.randint(min(self.a), max(self.a))
            sum += k  # Add 'k' (which matches 'a[i]') to the sum
        return sum / len(self.a)  # Calculate and return the unusual average

```

## Proof
<img width="max" alt="Screenshot 2023-09-26 at 16 48 22" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/f049b13a-3fc1-44f6-8c5a-1080b8ac139d">

## Testing
```.py
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
```
