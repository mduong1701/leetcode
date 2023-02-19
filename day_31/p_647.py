class Solution:
    # def countSubstrings(self, s: str) -> int:
    #     result = 0
    #     for i in range(len(s)):
    #         left = i
    #         right = i
    #         while left >= 0 and right < len(s) and s[left] == s[right]:
    #             result += 1
    #             left -= 1
    #             right += 1
    #         left = i
    #         right = i + 1
    #         while left >= 0 and right < len(s) and s[left] == s[right]:
    #             result += 1
    #             left -= 1
    #             right += 1
    #     return result

    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += self.isPal(s, i, i)
            result += self.isPal(s, i, i + 1)
        return result

    def isPal(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count