def coinChange(coins, amount):
    result = [amount for _ in range(amount + 1)]
    result[0] = 0

    for coin in coins:
        