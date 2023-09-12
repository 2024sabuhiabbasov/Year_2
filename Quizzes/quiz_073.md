# Quiz 073
<img width="max" alt="Screenshot 2023-09-12 at 9 08 26" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/4dd4f442-ce37-4392-9f64-81d596935cac">

## Solution
```.py
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Initialize an empty routing table
routing_table = {}


# Function to check if a MAC address is valid
def is_valid_mac(mac):
    # Check if the MAC address has the correct format (12 hexadecimal characters separated by colons)
    return len(mac) == 17 and all(c in '0123456789ABCDEF:' for c in mac)


# Function to add a MAC address to the routing table
def add_to_routing_table(mac):
    # Check if the MAC address is valid
    if not is_valid_mac(mac):
        # Print a red and bold error message for an invalid MAC address
        print(Fore.RED + Style.BRIGHT + "Invalid MAC address format" + Style.RESET_ALL)
        return

    # Check if the MAC address already exists in the routing table
    if mac in routing_table:
        # Print a yellow and bold message for an existing MAC address entry
        print(
            Fore.YELLOW + Style.BRIGHT + f"MAC: {mac}  IP: {routing_table[mac]} (Already in the routing table)" + Style.RESET_ALL)
        return

    # Find the next available IP address
    next_ip = "192.168.0." + str(len(routing_table) + 1)

    # Add the MAC address and IP address to the routing table
    routing_table[mac] = next_ip

    # Display the updated routing table
    print_routing_table()

    # Print a green and bold message for the newly assigned IP address
    print(Fore.GREEN + Style.BRIGHT + f"Assigned IP address {next_ip} to MAC address {mac}" + Style.RESET_ALL)


# Function to display the routing table
def print_routing_table():
    # Print a cyan and bold title for the routing table
    print(Fore.CYAN + Style.BRIGHT + "Routing Table:")
    print("{:<20} | {:<15}".format("MAC Address", "IP Address"))
    print("-" * 36)

    for mac, ip in routing_table.items():
        print("{:<20} | {:<15}".format(mac, ip))
    print()


# Main program loop
while True:
    mac_address = input("Enter a MAC address (format: 00:1A:2B:3C:4D:5E): ")
    add_to_routing_table(mac_address)
```
![IMG_4214](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/f371786c-bd52-4d0c-a435-1b7e16b2f09b)
![IMG_4215](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/52b69dd7-0d2d-419f-b432-eb36ba84ff06)

## Proof
<img width="max" alt="Screenshot 2023-09-12 at 13 23 57" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/225d54e2-c249-4c5f-bd86-81440f112ff1">
