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
            first = minHeap[0]

            for card in range(first, first + groupSize):
                if card not in minHeap:
                    return False
                
                count[card] -= 1

                if count[card] == 0:
                    

