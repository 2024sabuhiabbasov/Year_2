def profit(sales: list) -> int:
    min_profit = 99999999
    max_profit = -1
    for profits in sales:
        if profits < min_profit:
            min_profit = profits
        if profits > max_profit:
            max_profit = profits
    difference = max_profit - min_profit
    return difference


sales = [100, 45, 12, 3, 56, 7]

output = profit(sales)
print(output)
