import collections


class DetectSquares:

    def __init__(self):
        self.pointCount = collections.defaultdict(int)
        self.points = []

    def add(self, point):
        self.pointCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point):