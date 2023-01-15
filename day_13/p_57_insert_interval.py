def insert(intervals, newInterval):
    result = []

    for i in len(intervals):
        if newInterval[1] < intervals[i][0]:
            return newInterval + intervals[i:]
        elif 