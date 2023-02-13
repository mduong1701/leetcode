def minMeetingRooms(intervals):
    startTimes = sorted([ interval[0] for interval in intervals])
    endTimes = sorted([ interval[1] for interval in intervals])

    start = 0
    end = 0

    result = 0
    count = 0

    while start < len(startTimes):
        if startTimes[start] < endTimes[end]:
            count += 1
            start += 1
        else:
            count -= 1
            end += 1
        
        result = max(result, count)

    return result
