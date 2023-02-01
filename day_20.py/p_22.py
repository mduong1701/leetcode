def generateParenthesis(n):
    stack = []
    result = []

    def backtrack(numO, numC):
        if numO == numC == n:
            result.append("".join(stack))
            return
        
        if numO < n:
            stack.append("(")
            backtrack(numO + 1, numC)
            stack.pop()

        if numC < numO:
            stack.append(")")
            backtrack(numO, numC + 1)
            stack.pop()

    backtrack(0, 0)

    return result
