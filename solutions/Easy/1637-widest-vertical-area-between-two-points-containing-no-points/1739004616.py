class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        vals = sorted([x for (x,y) in points])

        return max([b-a for a,b in zip(vals, vals[1:])])
        