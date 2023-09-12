# Quiz 069

<img width="max" alt="Screenshot 2023-09-03 at 15 39 07" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/4645be97-e3b4-428b-b012-5e966a203f63">

## Solution
<img width="max" alt="Screenshot 2023-09-03 at 16 25 40" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/0a0dda7c-6ff2-456c-be6b-bc6c4e7185da">

```python
class ProfitCalculator:
    def __init__(self, sales):
        self.sales = sales

    def calculate_profit_difference(self):
        min_profit = 99999999  # Initialize the minimum profit with a high value
        max_profit = -1  # Initialize the maximum profit with a low value

        for profit in self.sales:  # Loop through the list of profits
            if profit < min_profit:  # If the profit is less than the current minimum
                min_profit = profit  # Update the minimum profit
            if profit > max_profit:  # If the profit is greater than the current maximum
                max_profit = profit  # Update the maximum profit

        difference = max_profit - min_profit  # Calculate the difference between the highest and lowest profits
        return difference  # Return the difference

    def custom_message(self):
        difference = self.calculate_profit_difference()
        return f"The difference between the highest and lowest profits: {difference}"

# Example usage
sales = [100, 45, 12, 3, 56, 7]
profit_calculator = ProfitCalculator(sales)  # Create an instance of the ProfitCalculator class

# Get the custom message and print it
message = profit_calculator.custom_message()
print(message)  # Output the custom message with the result
```

## Proof
<img width="max" alt="Screenshot 2023-09-03 at 15 37 46" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/8a0eb45e-e0e8-42ed-9afd-e585d91e95d1">
