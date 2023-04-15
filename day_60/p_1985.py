import heapq

class Solution:
    def kthLargestNumber(self, nums, k):
        maxHeap = [-1 * int(num) for num in nums]
        heapq.heapify(maxHeap)
        
        while maxHeap:
            tmp = heapq.heappop(maxHeap)
            k -= 1
            if k == 0:
                return str(-1 * tmp)