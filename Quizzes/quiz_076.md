# Quiz 076
<img width="max" alt="Screenshot 2023-09-12 at 8 53 14" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/539044aa-bbfa-4520-985b-beb4e16f9fc1">

## Solution
```.py
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
```
![IMG_4211](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/2efc2154-e1d6-4fa5-ab15-f724bba9b0ee)

## Proof for a case with an error
<img width="max" alt="Screenshot 2023-09-12 at 8 56 33" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/3f35e329-36c5-48e2-8f09-121a639d9160">

## Proof for a case without an error
<img width="max" alt="Screenshot 2023-09-12 at 8 57 04" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/b6407566-3876-442f-8505-49b4fdc29d77">
