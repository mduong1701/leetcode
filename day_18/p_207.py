def courseSchedule(numCourses, prerequisites):
    # Create a dictionary 
    courseMap = { i : [] for i in range(numCourses)}
    # Build the dictionary
    for second, first in prerequisites:
        courseMap[second].append(first)
    # Initialize a visited set
    visited = set()
    # DFS function
    def dfs(currentCourse):
        if currentCourse in visited:
            return False
        if courseMap[currentCourse] == []:
            return True

        visited.add(currentCourse)

        for prere in courseMap[currentCourse]:
            if not dfs(prere):
                return False
        
        visited.remove(currentCourse)

        return True

    for course in range(numCourses):
        
