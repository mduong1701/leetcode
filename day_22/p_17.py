def letterCombinations(digits):
    numberLetterMap = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }

    answer = []

    def dfs(index, newString):
        # "2" "3"
        if len(newString) == len(digits):
            answer.append(newString)
            return
        
        for character in numberLetterMap[digits[index]]:
            dfs(index + 1, newString + character)
            
    if digits:
        dfs(0, "")
    
    return answer