from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


class RoutingTable:
    def __init__(self):
        self.routing_table = {}

    # Function to check if a MAC address is valid
    def is_valid_mac(self, mac):
        # Check if the MAC address has the correct format (12 hexadecimal characters separated by colons)
        return len(mac) == 17 and all(c in '0123456789ABCDEF:' for c in mac)

    # Function to add a MAC address to the routing table
    def add_to_routing_table(self, mac):
        # Check if the MAC address is valid
        if not self.is_valid_mac(mac):
            # Print a red and bold error message for an invalid MAC address
            print(Fore.RED + Style.BRIGHT + "Invalid MAC address format" + Style.RESET_ALL)
            return

        # Check if the MAC address already exists in the routing table
        if mac in self.routing_table:
            # Print a yellow and bold message for an existing MAC address entry
            print(
                Fore.YELLOW + Style.BRIGHT + f"MAC: {mac}  IP: {self.routing_table[mac]} (Already in the routing table)" + Style.RESET_ALL)
            return

        # Find the next available IP address
        next_ip = "192.168.0." + str(len(self.routing_table) + 1)

        # Add the MAC address and IP address to the routing table
        self.routing_table[mac] = next_ip

        # Display the updated routing table
        self.print_routing_table()

        # Print a green and bold message for the newly assigned IP address
        print(Fore.GREEN + Style.BRIGHT + f"Assigned IP address {next_ip} to MAC address {mac}" + Style.RESET_ALL)

    # Function to display the routing table
    def print_routing_table(self):
        # Print a cyan and bold title for the routing table
        print(Fore.CYAN + Style.BRIGHT + "Routing Table:")
        print("{:<20} | {:<15}".format("MAC Address", "IP Address"))
        print("-" * 36)

        for mac, ip in self.routing_table.items():
            print("{:<20} | {:<15}".format(mac, ip))
        print()


routing_table = RoutingTable()

# Main program loop
while True:
    mac_address = input("Enter a MAC address (format: 00:1A:2B:3C:4D:5E): ")
    routing_table.add_to_routing_table(mac_address)
