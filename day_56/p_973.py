import heapq

class Solution:
    def kClosest(self, points, k):
        # points = [[3,3],[5,-1],[-2,4]], k = 2

        minHeap = []
        result = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)

        while k > 0:
            _ , xResult, yResult = heapq.heappop(minHeap)
            result.append([xResult, yResult])
            k -= 1

        return result
