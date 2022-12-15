def maxProfit(prices):
    profit = 0
    maxProfit = 0
    buy = 0
    sell = 1

    while sell < len(prices):
        profit = prices[sell] - prices[buy]
        if profit <= 0:
            buy = sell
        maxProfit = max(maxProfit, profit)
        sell += 1


    
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
    
