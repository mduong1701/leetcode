from collections import deque

class Solution:
    def canReach(self, s, minJump, maxJump):
        q = deque([0])
        farthest = 0

        