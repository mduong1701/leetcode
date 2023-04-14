import heapq

class Solution:
    def kthLargestNumber(self, nums, k):
        maxHeap = heapq.heapify([-1 * int(num) for num in nums])
        result = 0
        while maxHeap:
            tmp = maxHeap.heappop()
            k -= 1
            if k == 0:
                return str(-1 * tmp)