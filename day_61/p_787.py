class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
        prices = [float('inf')] * n
        # [ inf inf inf ]
        prices[src] = 0
        # [ 0 inf inf ]
        for _ in range(k + 1):
            pricesTemp = prices.copy()
            # [ 0 inf inf ]
            for source, destination, price in flights:
                if pricesTemp[source] == float('inf'):
                    continue

                if pricesTemp[source] + price < pricesTemp[destination]:
                    pricesTemp[destination] = pricesTemp[source] + price

            prices = pricesTemp

        return prices[dst] if prices[dst] != float('inf') else -1
