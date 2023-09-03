# Quiz 069

One array holds the daily sales of a clothing store in no particular order. You are tasked with finding the profit of the best day in comparison to the worst day. That is, how much more was sold in Japanese Yens the best day?

## Solution
```python
# Define a function that takes a list of sales and returns the difference between the highest and lowest profits.
def profit(sales: list) -> int:
    min_profit = 99999999  # The highest number to compare with the profits
    max_profit = -1  # The lowest number to compare with the profits
    for profits in sales:  # Loop through the list of sales
        if profits < min_profit:  # If the profits is less than the min_profit
            min_profit = profits  # Assign the profits to the min_profit
        if profits > max_profit:  # If the profits is greater than the max_profit
            max_profit = profits  # Assign the profits to the max_profit
    difference = max_profit - min_profit  # Calculate the difference between the highest and lowest profits
    return difference  # Return the difference


sales = [100, 45, 12, 3, 56, 7]  # List of sales

output = profit(sales)  # Call the function and assign the return value to the output variable
print(output)  # Output the result
```

