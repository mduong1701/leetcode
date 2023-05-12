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
                return nodesDictionary[numberOfNodes]

            result = []

            for leftNum in range(numberOfNodes):
                rightNum = numberOfNodes - 1 - leftNum

                leftBranch = backtracking(leftNum)
                rightBranch = backtracking(rightNum)

                for left in leftBranch:
                    for right in rightBranch:
                        result.append(TreeNode(0, left, right))

            nodesDictionary[numberOfNodes] = result

            return result

        return backtracking(n)