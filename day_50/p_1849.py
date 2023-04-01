class Solution:
    def splitString(self, s):
        for i in range(len(s) - 1):
            value = int(s[ : i + 1])
            if dfs(i + 1, value):
                return True
        return False
