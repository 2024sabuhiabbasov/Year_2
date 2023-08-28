# Quiz 071
<img width="max" alt="Screenshot 2023-08-28 at 15 11 21" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/fbc82d4b-8a27-439a-8f06-f27fd8b819ac">

## Solution

```python
import random
import time

# Define a class to generate IPv6 addresses
class ipv6machine():
    def __init__(self, number: int):
        self.number = number

    # Function to generate a random sixtec (part of an IPv6 address)
    def sixtec_generator(self):
        # Define the characters used in IPv6 representation
        characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']
        ip_address = ''

        # Generate each sixtec
        for i in range(0, 8):
            sixtec = ''
            for j in range(0, 4):
                # Generate a random number between 0 and 15 (hexadecimal)
                random_num = random.randint(0, 15)
                # Add the randomly selected character to the sixtec
                sixtec = sixtec + characters[random_num]
            ip_address = ip_address + sixtec
            # Add a colon between sixtecs except for the last one
            if i != 7:
                ip_address = ip_address + ':'

        # Return the generated IPv6 address
        return ip_address

    # Function to generate a list of unique IPv6 addresses
    def list_generator(self):
        ip_list = []

        # Generate the specified number of unique IPv6 addresses
        for i in range(0, self.number):
            ip = self.sixtec_generator()

            # Ensure generated IP is unique within the list
            while ip in ip_list:
                ip = self.sixtec_generator()

            # Append the unique IP to the list
            ip_list.append(ip)

        # Return the list of generated unique IPv6 addresses
        return ip_list


# Get user input for the number of IPv6 addresses to generate
n = int(input("Please enter the number of IPv6 addresses you want to print: "))

# Create an instance of the ipv6machine class
ipv6 = ipv6machine(n)

# Generate a list of unique IPv6 addresses
ipv6_list = ipv6.list_generator()

# Print the generated IPv6 addresses along with their index
for i, ip in enumerate(ipv6_list, start=1):
    print(f"{i}: {ip}")
```