# Quiz 075
<img width="max" alt="Screenshot 2023-09-12 at 8 59 27" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/e31279f0-d1be-4984-be7a-7a598c2ccd2e">

## Solution
```.py
class converter:
    def __init__(self, data: str):
        self.data = data  # Initialize the data
        self.ascii_codes = []  # Initialize the ascii codes
        self.binary = ''  # Initialize the binary which is going to be returned
        for letter in self.data:  # Iterate through the data and append the ascii codes of the letters to the list
            self.ascii_codes.append(ord(letter))

    def binary_generator(self):  # Define a function that generates the binary for the ascii codes
        for number in self.ascii_codes:  # Iterate through the ascii codes
            binary = ''  # Initialize the binary
            while number > 0:  # Loop until the number is greater than 0
                binary = str(number % 2) + binary  # Add the remainder of the number to the binary
                number = number // 2  # Divide the number by 2 and assign the result to the number
            if len(binary) < 8:  # If the length of the binary is less than 8
                binary = '0' * (8 - len(binary)) + binary  # Add 0s to the beginning of the binary
            self.binary = self.binary + binary + ' '  # Add the binary to the binary list

        return self.binary  # Return the binary


data = input("Enter a string to convert to binary: ")  # Get the data from the user
convert = converter(data)  # Create an instance of the converter class
output = convert.binary_generator()  # Call the binary_generator method and assign the return value to the output
# variable
print(output)  # Output the result
```
![IMG_4212](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/6c42ac13-f779-4456-891c-738c12fa2a36)

## Proof
<img width="max" alt="Screenshot 2023-09-12 at 9 01 10" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/b2c4219d-fc20-49d6-9ca8-13534e039092">
<img width="max" alt="Screenshot 2023-09-12 at 9 01 39" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/8dca7cad-5e7f-4df1-83ff-3413b2039301">
