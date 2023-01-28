def coinChange(coins, amount):
    result = [amount + 1 for _ in range(amount + 1)]
    result[0] = 0

    for coin in coins:
        for i in range(coin, len(result)):
            result[i] = min(result[i], 1 + result[i - coin])
    
    return result[-1] if result[-1] != amount + 1 else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))