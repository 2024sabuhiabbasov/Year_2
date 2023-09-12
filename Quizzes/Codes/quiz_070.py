# Function to generate IPv4 addresses
def generate_ipv4():
    addresses = []
    total_addresses = 256 ** 4

    for i in range(256):
        for j in range(256):
            for k in range(256):
                for l in range(256):
                    address = f"{i}.{j}.{k}.{l}"
                    addresses.append(address)

                    # Print the first 20 generated addresses as an example
                    if len(addresses) <= 20:
                        print(f"Generated IP: {address}")

    return addresses


# Call the function to generate IPv4 addresses
output = generate_ipv4()

# Print a new line to separate progress from the final result
print("\n")

# Print the list of generated IPv4 addresses
print(output)
