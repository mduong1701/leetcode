def asteroidCollision(asteroids):
    stack = []

    for asteroid in asteroids:

        while stack and stack[-1] > 0 and asteroid < 0:
            collision = stack[-1] + asteroid

            if collision > 0: # 10 vs -5
                asteroid = 0
            elif collision < 0: # 10 vs -15
                stack.pop()
            else: # 10 vs -10
                stack.pop()
                asteroid = 0
        if asteroid:
            stack.append(asteroid)

    return stack

print(asteroidCollision([5,10,-5]))