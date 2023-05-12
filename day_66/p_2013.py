import collections


class DetectSquares:

    def __init__(self):
        self.pointCount = collections.defaultdict(int)
        self.points = []

    def add(self, point):
        self.pointCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point):
        result = 0
        px, py = point

        for x, y in self.points:
            if abs(x - px) != abs(y - py) or px == x or py == y:
                continue

            result += self.pointCount[(x, py)] * self.pointCount[(px, y)]

        return result