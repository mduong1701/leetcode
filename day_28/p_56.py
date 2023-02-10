def merge(intervals):
    result = [intervals[0]]

    for start, end in intervals[1:]:
        