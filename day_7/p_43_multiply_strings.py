def multiply(num1, num2):

    if "0" in [num1, num2]:
        return "0"
    
    len1 = len(num1)
    len2 = len(num2)

    result = [0] * (len1 + len2)

    num1 = num1[::-1]
    num2 = num2[::-1]
    
    for i in range(len1):
        for j in range(len2):
            product = int(num1[i]) * int(num2[j])
            result[i + j] += product
            result[i + j + 1] += (result[i + j] // 10)
            result[i + j] = result[i + j] % 10

    result = result[::-1]
    beginning = 0
    # while beginning < len(result) and result[beginning] == 0:
    while result[beginning] == 0:
        beginning += 1

    result = map(str, result[beginning:])

    return "".join(result)

print(multiply("123", "456"))
    