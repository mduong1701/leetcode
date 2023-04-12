# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        result = []
        queue = collections.deque([root])

        while queue:
            rightNode = None
            queueLength = len(queue)

            for i in range(queueLength):
                node = queue.popleft()
                if node:
                    rightNode = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightNode:
                result.append(rightNode.val)
                
        return result