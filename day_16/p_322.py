def coinChange(coins, amount):
    result = [amount for _ in range(amount + 1)]
    result[0] = 0

    for coin in coins:
        for i in range(coin, len(result)):
            result[i] = min(result[i], 1 + result[i - coin])
    
    return result[-1] if result[-1] != amount else -1

