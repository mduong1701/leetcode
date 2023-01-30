def courseSchedule(numCourses, prerequisites):
    # Create a dictionary 
    courseMap = { i : [] for i in range(numCourses)}
    # Build the dictionary
    for second, first in prerequisites:
        courseMap[second].append(first)
    
