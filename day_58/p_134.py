class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1

        result = 0
        total = 0
        
        for i in range(len(gas)):
