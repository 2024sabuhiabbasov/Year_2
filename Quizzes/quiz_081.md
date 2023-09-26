# Quiz 081

<img width="max" alt="Screenshot 2023-09-26 at 16 51 21" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/a66a6541-df5d-469c-95ff-aeccd7858adc">

## Solution
![IMG_4714](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/f0174892-8177-4d26-9a08-058bee1421eb)

![image](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/fe81f58d-f637-4915-ac9a-45d8db48c4b8)

```.py
class EmployeeSorter:
    def __init__(self, names):
        self.names = names

    def bubble_sort(self):
        n = len(self.names)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Extract the last names for comparison
                last_name1 = self.names[j].split(", ")[0]
                last_name2 = self.names[j + 1].split(", ")[0]

                # Compare and swap if necessary
                if last_name1 > last_name2:
                    self.names[j], self.names[j + 1] = self.names[j + 1], self.names[j]

    def get_sorted_names(self):
        return self.names
```

## Proof
<img width="max" alt="Screenshot 2023-09-26 at 17 02 57" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/86bf9764-3479-4b84-b4ee-12d73d6f1b91">

## Testing
```.py
import pytest
from Quizzes.Codes.quiz_081 import EmployeeSorter


# Test cases for the EmployeeSorter class

def test_bubble_sort_with_single_name():
    # Test sorting a list with a single name (no change expected)
    sorter = EmployeeSorter(["Smith, John"])
    sorter.bubble_sort()
    assert sorter.get_sorted_names() == ["Smith, John"]


def test_bubble_sort_with_already_sorted_names():
    # Test sorting a list with already sorted names (no change expected)
    names = ["Doe, Jane", "Smith, John", "Williams, Alice"]
    sorter = EmployeeSorter(names.copy())  # Create a copy to avoid modifying the original list
    sorter.bubble_sort()
    assert sorter.get_sorted_names() == names


def test_bubble_sort_with_unsorted_names():
    # Test sorting a list with unsorted names
    names = ["Smith, John", "Williams, Alice", "Doe, Jane"]
    sorter = EmployeeSorter(names.copy())  # Create a copy to avoid modifying the original list
    sorter.bubble_sort()
    expected_sorted_names = ["Doe, Jane", "Smith, John", "Williams, Alice"]
    assert sorter.get_sorted_names() == expected_sorted_names


def test_bubble_sort_with_reverse_sorted_names():
    # Test sorting a list with names sorted in reverse order
    names = ["Williams, Alice", "Smith, John", "Doe, Jane"]
    sorter = EmployeeSorter(names.copy())  # Create a copy to avoid modifying the original list
    sorter.bubble_sort()
    expected_sorted_names = ["Doe, Jane", "Smith, John", "Williams, Alice"]
    assert sorter.get_sorted_names() == expected_sorted_names


if __name__ == "__main__":
    pytest.main()
```
