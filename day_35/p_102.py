import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        queue = collections.deque()
        queue.append(root)

        result = []

        while queue:
            level = []
            queueLength = len(queue)

            for _ in range(queueLength):
                node = queue.popleft()
