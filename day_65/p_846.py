import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize):

        if len(hand) % groupSize != 0:
            return False

        count = {}

        for card in hand:
            count[card] = 1 + count.get(card, 0)

        minHeap = list(count.keys)
        heapq.heapify(minHeap)

        while minHeap:


