# Quiz 069

<img width="max" alt="Screenshot 2023-09-03 at 15 39 07" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/4645be97-e3b4-428b-b012-5e966a203f63">

## Solution
<img width="max" alt="Screenshot 2023-09-03 at 16 25 40" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/0a0dda7c-6ff2-456c-be6b-bc6c4e7185da">

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

## Proof
<img width="max" alt="Screenshot 2023-09-03 at 15 37 46" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/8a0eb45e-e0e8-42ed-9afd-e585d91e95d1">
