# Quiz 078

<img width="max" alt="Screenshot 2023-09-14 at 13 48 48" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/f51ee76a-0d21-4c8c-9611-e4b2cf3ce076">

## Solution
![IMG_4225](https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/74941ed3-7903-4604-b65e-0ee2cd3f7ba4)

```.py
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
```

## Proof
### Case with a port number of 80
<img width="max" alt="Screenshot 2023-09-14 at 13 51 06" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/01e86856-95c0-4c7e-9476-55f9b79ff65b">

### Case with a port number of 22123
<img width="max" alt="Screenshot 2023-09-14 at 13 52 10" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/f1081ca6-8c90-4462-90f2-ae4bdcdefff2">

### Case with a port number of 100
<img width="max" alt="Screenshot 2023-09-14 at 13 53 04" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/adb24ef8-cb8b-4995-8ece-81b762e670f1">
