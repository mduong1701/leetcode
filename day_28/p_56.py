def merge(intervals):

    intervals.sort(key = lambda inter : inter[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        if result[-1][1] >= start:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    
    return result