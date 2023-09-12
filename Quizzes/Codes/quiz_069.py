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
