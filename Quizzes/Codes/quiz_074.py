# Import the 'ceil' function from the 'math' module
from math import ceil


# Define a function named 'build_data_pkg' that takes five input strings
def build_data_pkg(mac_rx: str, ip_rx: str, mac_sx: str, ip_sx: str, data: str):
    # Create a string 'ip_mac' by concatenating MAC and IP addresses with '|' separator
    ip_mac = f"{mac_rx}|{ip_rx}|{mac_sx}|{ip_sx}|"
    output = []  # Initialize an empty list 'output'
    length = ceil(
        len(data) / 4)  # Calculate the number of iterations based on data length (ceil is used for rounding up)

    # Iterate through the data in chunks of 4 characters
    for i in range(length):
        load = data[:4]  # Extract the first 4 characters of 'data' or less if the remaining length is less than 4
        if len(load) < 4:
            load = data  # If the chunk is less than 4 characters, use the entire 'data'
        data = data[4:]  # Remove the processed chunk from 'data'
        output.append(f"{ip_mac}{i}|{load}")  # Create a formatted string and append it to 'output'

    return output  # Return the list of formatted strings


# Call the 'build_data_pkg' function with example input
data_package = build_data_pkg("8C:31:03:4F:CE:DB", "192.168.0.1", "7A:7A:A7:C2:44:FB", "192.168.0.2", "Hello world")

# Print the resulting data package list
print(data_package)
