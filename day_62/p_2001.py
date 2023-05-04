class Solution:
    def interchangeableRectangles(self, rectangles):
        count = {}

        for width, height in rectangles:
            count[width / height] = 1 + count.get(width / height, 0)

        for times in count.values():
            