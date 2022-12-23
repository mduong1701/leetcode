import heapq

def lastStoneWeight(stones):
    newStones = [-s for s in stones]
    heapq.heapify(newStones)
    while len(newStones) > 1:
        heaviest = heapq.heappop(newStones)
        second = heapq.heappop(newStones)
        if second > heaviest:
            heapq.heappush(newStones, heaviest - second)
    newStones.append(0)
    return abs(newStones[0])

print(lastStoneWeight([1,9,2,8,3,7,4,6,5]))


