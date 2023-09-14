class layer4_firewall:
    def __init__(self, data: str):
        self.data = data

    def msg(self):
        port_bits = self.data[:16]  # Extract the first 16 bits as the port number
        port_number = int(port_bits, 2)  # Convert the first 16 bits to an integer
        print(port_number)
        if port_number == 80 or port_number == 22123:
            return "Allowed", self.data[16:]
        else:
            return "Filtered", "None"


layer_4 = layer4_firewall("00000000010100001011")  # 80

status, message = layer_4.msg()
print(f"{status}, {message}")
