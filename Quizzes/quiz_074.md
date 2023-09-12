# Quiz 074
<img width="944" alt="Screenshot 2023-09-12 at 9 02 54" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/33ad6f27-7963-438a-b11d-b5914b406877">

## Solution
```.py
from math import ceil

class DataPackageBuilder:
    def __init__(self, mac_rx, ip_rx, mac_sx, ip_sx, data):
        self.mac_rx = mac_rx
        self.ip_rx = ip_rx
        self.mac_sx = mac_sx
        self.ip_sx = ip_sx
        self.data = data

    def build_data_pkg(self):
        # Concatenate MAC and IP addresses with '|' separator
        ip_mac = f"{self.mac_rx}|{self.ip_rx}|{self.mac_sx}|{self.ip_sx}|"
        output = []  # Initialize an empty list to store data packages
        length = ceil(len(self.data) / 4)  # Calculate the number of iterations based on data length (rounding up)

        # Iterate through the data in chunks of 4 characters
        for i in range(length):
            load = self.data[:4]  # Extract the first 4 characters of 'data' or less if remaining length is < 4
            if len(load) < 4:
                load = self.data  # If the chunk is less than 4 characters, use the entire 'data'
            self.data = self.data[4:]  # Remove the processed chunk from 'data'
            output.append(f"{ip_mac}{i}|{load}")  # Create a formatted string and append it to 'output'

        return output  # Return the list of formatted strings


# Example usage
data_package_builder = DataPackageBuilder(
    "8C:31:03:4F:CE:DB",
    "192.168.0.1",
    "7A:7A:A7:C2:44:FB",
    "192.168.0.2",
    "Hello world"
)

data_package = data_package_builder.build_data_pkg()
print(data_package)
```
![IMG_4213](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/0d2c2432-1f5a-4aad-8852-8b2fc769074f)

## Proof
<img width="max" alt="Screenshot 2023-09-12 at 13 38 14" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/b59416db-4afc-471e-a85d-9a839592d537">

Continues:

<img width="max" alt="Screenshot 2023-09-12 at 9 06 06" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/8df72d67-5e7d-41b0-843b-a8b2f6058a0f">
