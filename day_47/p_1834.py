class Solution:
    def getOrder(self, tasks):
        for i in range(len(tasks)):
            tasks[i].append(i)
            
        tasks.sort(key = lambda task : task[0])