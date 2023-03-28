import heapq

class Solution:
    def getOrder(self, tasks):
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort(key = lambda task : task[0])

        result = []
        minHeap = []

        i = 0
        time = 0

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1

            