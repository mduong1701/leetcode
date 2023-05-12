# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n):
        nodesDictionary = {0: [], 1: [TreeNode()]}

        def backtracking(numberOfNodes):
            if numberOfNodes in nodesDictionary:
                return nodesDictionary[nodesDictionary]

            