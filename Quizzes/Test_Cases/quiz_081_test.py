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
