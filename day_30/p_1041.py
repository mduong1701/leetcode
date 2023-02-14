def isRobotBounded(self, instructions):
    dirX, dirY = 0, 1
    x, y = 0, 0

    for instruction in instructions:
        if instruction == "G":
            x += dirX
            y += dirY
        elif instruction == "L":
            dirX, dirY = -1 * dirY, dirX
        else:
            dirX = dirY
            dirY = -1 * dirX

    return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)