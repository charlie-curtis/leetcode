class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        intervals = []
        d = {}
        d[0] = -1

        ssum = 0
        for i,x in enumerate(nums):
            ssum+=x
            if ssum-target in d:
                intervals.append([d[ssum-target]+1, i])

            d[ssum] = i

        out = []
        for s,e in intervals:
            if not out or out[-1][1] < s:
                out.append([s,e])
        return len(out)
        