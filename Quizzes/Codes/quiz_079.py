# Define a class called 'palindromic' to work with palindromic numbers.
class palindromic:
    def __init__(self, a: int, b: int):
        # Initialize the class with two integers 'a' and 'b'.
        self.a = a
        self.b = b
        # Create an empty list to store palindromic numbers.
        self.palindromic_list = []

    # A method to reverse an integer.
    def reverser(self, number: int):
        # Convert the number to a string for easier reversal.
        number = str(number)
        number = list(number)
        reversed_number = ''
        # Iterate through the digits in reverse order and build the reversed number.
        for i in range(len(number) - 1, -1, -1):
            reversed_number += number[i]
        return int(reversed_number)

    # A method to check if a number is palindromic.
    def reverse_checker(self, number: int):
        return number == self.reverser(number)

    # A method to generate a list of palindromic numbers in the given range [a, b].
    def list_generator(self):
        for i in range(self.a, self.b + 1):
            if self.reverse_checker(i):
                self.palindromic_list.append(i)
        # Return the list of palindromic numbers.
        return self.palindromic_list


# Create an instance of the 'palindromic' class with range [1, 999].
palindromic_numbers = palindromic(1, 99)
# Generate a list of palindromic numbers in the specified range.
list_of_palindromic_numbers = palindromic_numbers.list_generator()
# Print the list of palindromic numbers.
print(list_of_palindromic_numbers)
