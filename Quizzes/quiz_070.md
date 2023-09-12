# Quiz 070

<img width="max" alt="Screenshot 2023-09-03 at 16 31 02" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/1a0d4121-8110-4f64-a93e-1efee6d0625c">

## Solution
<img width="max" alt="Screenshot 2023-09-03 at 16 31 42" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/d1835c80-6e8a-4409-8c27-af067dfaaf33">

```.py
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

                    # Print the first 10 generated addresses as an example
                    if len(addresses) <= 20:
                        print(f"Generated IP: {address}")

    return addresses


# Call the function to generate IPv4 addresses
output = generate_ipv4()

# Print a new line to separate progress from the final result
print("\n")

# Print the list of generated IPv4 addresses
print(output)
```

## Proof
<img width="max" alt="Screenshot 2023-09-12 at 13 55 37" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/20db436c-ed27-43f6-b898-bcd7fea67999">

