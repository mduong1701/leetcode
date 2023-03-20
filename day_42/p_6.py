class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        result = ""

        for row in range(numRows):
            increment = numRows * 2 - 2
            for i in range(row, len(s), increment):
                result += s[i]

                if row > 0 and \
                    row < numRows - 1 and \
                    (i + increment - 2 * row) < len(s):
                    result += s[i + increment - 2 * row]

        return result
