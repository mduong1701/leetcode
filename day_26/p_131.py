def isPal(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return  True

def partition(s):
    result = []
    partition = []

    def dfs(index):
        