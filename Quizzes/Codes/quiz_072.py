import random


# Define a class to generate MAC addresses
class MacAddressGenerator:
    def __init__(self, number: int):
        self.number = number

    # Function to generate a random MAC address
    def mac_address_generator(self):
        mac_address = []

        # Generate six pairs of random hexadecimal digits
        for _ in range(6):
            hex_pair = ''.join(random.choice('0123456789ABCDEF') for _ in range(2))
            mac_address.append(hex_pair)

        # Join the pairs with colons to form the MAC address
        formatted_mac = ':'.join(mac_address)

        return formatted_mac

    # Function to generate a list of unique MAC addresses
    def list_generator(self):
        mac_list = []

        # Generate the specified number of unique MAC addresses
        for _ in range(self.number):
            mac = self.mac_address_generator()

            # Ensure generated MAC is unique within the list
            while mac in mac_list:
                mac = self.mac_address_generator()

            # Append the unique MAC to the list
            mac_list.append(mac)

        # Return the list of generated unique MAC addresses
        return mac_list


# Get user input for the number of MAC addresses to generate
n = int(input("Please enter the number of MAC addresses you want to generate: "))

# Create an instance of the MacAddressGenerator class
mac_generator = MacAddressGenerator(n)

# Generate a list of unique MAC addresses
mac_list = mac_generator.list_generator()

# Print the generated MAC addresses along with their index
for i, mac in enumerate(mac_list, start=1):
    print(f"{i}: {mac}")
