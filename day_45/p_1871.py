from collections import deque

class Solution:
    def canReach(self, s, minJump, maxJump):
        q = deque([0])
        farthest = 0

        while q:
            index = q.popleft()
            start = max(index  + minJump, farthest)

            for current in range(start, min(start + maxJump+ 1, len(s))):
                if s[current] == "0":
                    q.append(current)
                    if current == len(s) - 1:
                        return True
                        