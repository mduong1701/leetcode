def findOrder(numCourses, prerequisites):
    prerequisiteMap = { c : [] for c in range(numCourses)}

    for course, first in prerequisites:
        prerequisiteMap[course].append(first)

    visited = set()
    cycle = set()
    result = []

    def dfs(course):
        if course in cycle:
            return False
        if course in visited:
            return True
        
        cycle.add(course)
        
        for pre in prerequisiteMap[course]:
            if dfs(pre) == False:
                return False

        cycle.remove(course)
        visited.add(course)
        result.append(course)
        
        return True

    for eachCourse in range(numCourses):
        if dfs(eachCourse) == False:
            return []

    return result