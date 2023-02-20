class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        result = [ 0 for _ in range(len(num1) + len(num2))]

        