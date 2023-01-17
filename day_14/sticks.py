def stickNum(sticks, k):

    resultArray = [k + 1] * (k + 1)
    resultArray[0] = 0

    for i in range(1, k + 1):
        for stick in sticks:
            if i >= stick:
                resultArray[i] = min(resultArray[i], 1 + resultArray[i - stick])
    
    if resultArray[-1] == k + 1:
        return -1
    
    return resultArray[-1]

print(stickNum([1,5,12], 13))
print(stickNum([1,14,30,17], 68))
print(stickNum([13,17,43,100,110,120], 109))