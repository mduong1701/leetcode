from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for string in strs:
            countArray = [0 for _ in range(26)]
            for character in string:
                countArray[ord(character) - ord("a")] += 1
            result[tuple(countArray)].append(string)

        return result.values()