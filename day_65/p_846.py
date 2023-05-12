import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize):
        count = {}

        for card in hand:
            count[card] = 1 + count.get(card, 0)

        minHeap = list(count.keys)
        heapq.heapify(minHeap)

        

