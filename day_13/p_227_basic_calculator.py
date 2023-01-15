def calculate(s):
    sign = "+"
    currentNumber = 0
    numberStack = []

    newS = s + "+"

    for character in newS:
        if character == " ":
            continue

        if character.isdigit():
            currentNumber = currentNumber * 10 + int(character)
        else:
            if sign == "+":
                numberStack.append(currentNumber)
            if sign == "-":
                numberStack.append(currentNumber * (-1))
            if sign == "*":
                numberStack.append(numberStack.pop() * currentNumber)
            if sign == "/":
                numberStack.append(numberStack.pop() // currentNumber)

            sign = character
            currentNumber = 0
    
    return sum(numberStack)

