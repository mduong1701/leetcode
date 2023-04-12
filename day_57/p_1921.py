import math

class Solution:
    def eliminateMaximum(self, dist, speed):
        # dist = [1,3,4], speed = [1,1,1]
        # minuteReached = [ 1, 3, 4]

        minuteReached = []
        for i in range(len(dist)):
            minuteReached.append(math.ceil(dist[i] / speed[i]))

        minuteReached.sort()
        result = 0
        for minute in range(len(minuteReached)):
            if minute >= minuteReached[minute]:
                return result

            result += 1

        return result