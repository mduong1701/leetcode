def calculate(s):
    sign = "+"
    currentNumber = 0
    numberStack = []

    newS = s + "+"

    for character in newS:
        if character == " ":
            continue

        