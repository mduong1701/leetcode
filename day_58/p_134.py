class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1

        