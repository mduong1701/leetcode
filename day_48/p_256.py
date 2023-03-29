class Solution:
    def minCost(self, costs):
        result = costs[0]

        for house in range(1, len(costs)):
            tempCosts = []
            for costIndex in range(len(costs[house])):
                temp = costs[house][costIndex] + min(result[:costIndex], result[costIndex + 1:])
                tempCosts.append(temp)
            

