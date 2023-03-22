class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x[0])

        for i in range(1, len(intervals)):
            interval1 = intervals[i - 1]
            interval2 = intervals[i]

            if interval1[1] > interval2[0]:
                return False

        return True
