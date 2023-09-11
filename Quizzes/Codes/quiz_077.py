# Define a class named 'checker'
class checker:
    # Constructor initializes the class with 'data' (a string)
    def __init__(self, data: str):
        self.data = data  # Store the input data
        self.error = False  # Initialize 'error' as False

    # Method for error checking
    def error_check(self):
        sum_of_ones = 0  # Initialize a counter for '1's
        first_letter = self.data[:1]  # Get the first character of 'data'
        self.data = self.data[1:]  # Remove the first character from 'data'

        # Iterate through the remaining characters in 'data'
        for letter in self.data:
            if letter == '1':
                sum_of_ones = sum_of_ones + 1  # Count '1's

        # Check if the count of '1's is even and the first character is '1'
        if sum_of_ones % 2 == 0 and first_letter == '1':
            return self.error  # Return False (no error)
        else:
            return self.error  # Return True (error)

# Create an instance of the 'checker' class with input data "101010101011"
error_checker = checker("101010101011")

# Call the 'error_check' method to check for errors and store the result
output = error_checker.error_check()

# Print the result (True if there is an error, False if not)
print(output)
