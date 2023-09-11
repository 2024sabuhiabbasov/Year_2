# Define a class named 'checker'
class checker:
    # Constructor initializes the class with 'data' (a string)
    def __init__(self, data: str):
        self.data = data  # Store the input data
        self.error = False  # Initialize 'error' as False

    # Method for error checking
    def error_check(self):
        length = len(self.data) // 3  # Calculate the length of each part
        data_arr = []  # Initialize an empty list to hold characters
        for letter in self.data:
            data_arr.append(letter)  # Append each character to the list

        # Split the data into three parts: original, copy_1, and copy_2
        original, copy_1, copy_2 = data_arr[:length], data_arr[length:length * 2], data_arr[length * 2:length * 3]

        # for i in range(0, length):
        #     if original[i] == copy_1[i] and copy_2[i] != original[i]:
        #         self.error = True
        #         pass
        #     elif original[i] == copy_2[i] and copy_1[i] != original[i]:
        #         self.error = True
        #         pass
        #     elif copy_1[i] == copy_2[i] and original[i] != copy_2[i]:
        #         self.error = True
        #         original[i] = copy_1[i]

        # Iterate through each character in the parts
        for i in range(length):
            # Check if the character in 'original' matches 'copy_1' or 'copy_2' but not both
            if (original[i] == copy_1[i] or original[i] == copy_2[i]) and copy_1[i] != copy_2[i]:
                self.error = True  # Set 'error' to True
                original[i] = copy_1[i]  # Update 'original' with 'copy_1'

        # Check if there was an error
        if self.error:
            return self.error, ''.join(original)  # Return True and the corrected string
        else:
            return self.error  # Return False (no error)


# Create an instance of the 'checker' class with input data "101010101011"
error_checker = checker("101010101011")

# Call the 'error_check' method to check for errors and store the result
output = error_checker.error_check()

# Print the result (True if there is an error, False if not, and the corrected string)
print(output)
