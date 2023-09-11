# Quiz 077
<img width="max" alt="Screenshot 2023-09-12 at 8 49 35" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/a1f1b8e8-9832-471e-9f3f-acdc01cc62cd">

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
        sum_of_ones = 0  # Initialize a counter for '1's
        first_letter = self.data[:1]  # Get the first character of 'data'
        self.data = self.data[1:]  # Remove the first character from 'data'

        # Iterate through the remaining characters in 'data'
        for letter in self.data:
            if letter == '1':
                sum_of_ones = sum_of_ones + 1 # Count '1's

        # Check if the count of '1's is even and the first character is '1',
        # or if the count is odd and the first character is '0'
        if (sum_of_ones % 2 == 0 and first_letter == '1') or (sum_of_ones % 2 == 1 and first_letter == '0'):
            return self.error  # Return False (no error)
        else:
            self.error = True  # Set 'error' to True
            # Flip the first character if there's an error
            first_letter = '0' if first_letter == '1' else '1'
            self.data = first_letter + self.data  # Correct the data
            return self.error, self.data  # Return True (error) and corrected data


# Create an instance of the 'checker' class with input data "000010001011"
error_checker = checker("101010001011")

# Call the 'error_check' method to check for errors and store the result
output = error_checker.error_check()

# Print the result (True if there is an error, False if not)
print(output)
```
![IMG_4210](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/27eeed19-89aa-4700-b642-0eea15135374)
## Proof for a case with an error
<img width="max" alt="Screenshot 2023-09-12 at 8 51 21" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/5e78d8fc-f519-4201-b529-5b05a3354985">

## Proof for a case without an error
<img width="max" alt="Screenshot 2023-09-12 at 8 52 02" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/94a5ce5e-2c6d-4772-9dc0-21eb5dff2bd7">
