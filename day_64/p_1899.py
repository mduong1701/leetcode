class Solution:
    def mergeTriplets(self, triplets, target):
        result = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            
