class layer4_firewall:
    def __init__(self, data: str):
        self.data = data

    def msg(self):
        # Extract the first 16 bits as the port number
        port_bits = self.data[:16]

        # Convert the first 16 bits to an integer
        port_number = int(port_bits, 2)
        print(f"Port number: {port_number}")

        # Check if the port number is 80 or 22123
        if port_number == 80 or port_number == 22123:
            return "Allowed", self.data[16:]
        else:
            return "Filtered", "None"


# Create an instance of the layer4_firewall class with the binary data
layer_4 = layer4_firewall("00000000011001001011")  # 80

# Call the msg method and retrieve the status and message
status, message = layer_4.msg()

# Print the status and message
print(f"{status}, {message}")
