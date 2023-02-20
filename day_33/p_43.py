class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        # "123" * "456" ---> [ 0 0 0 0 0 0]
        result = [ 0 for _ in range(len(num1) + len(num2))]

        # "1 2 3" ---> "3 2 1"
        #               i
        num1 = num1[::-1]
        # "4 5 6" ---> "6 5 4"
        #               j
        num2 = num2[::-1]
        # product     [ 0 0 0 0 0 0]
        for j in range(len(num2)):
            for i in range(len(num1)):
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product
                result[i + j + 1] += result[i + j] // 10
                result[i + j] = result[i + j] % 10

        result = result[::-1]
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        final = ""
        for i in range(start, len(result)):
            final += str(result[i])

        return "".join(final)