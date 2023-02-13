def minMeetingRooms(intervals):
    startTimes = sorted([ interval[0] for interval in intervals])
    endTimes = sorted([ interval[1] for interval in intervals])