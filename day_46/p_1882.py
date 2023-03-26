# available = [(weight, index)]
# unavailable = [(timeLeftToBeFree, weight, index)]

import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        result = [0 for _ in range(len(tasks))]

        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)
        unavailable = []

