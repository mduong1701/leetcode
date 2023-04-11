import heapq


class Solution:
    def kClosest(self, points, k):
        # points = [[3,3],[5,-1],[-2,4]], k = 2

        minHeap = []
        
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)
