class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        for i,x in enumerate(arr):

            if x == i: return i

        return -1
        