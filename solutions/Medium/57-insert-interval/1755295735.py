class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        out = []
        used = False

        def append(s,e):
            if not out or out[-1][1] < s:
                out.append([s,e])
            else:
                out[-1] = [out[-1][0], max(out[-1][1], e)]

        for s,e in intervals:
            if newInterval[0] <= s and not used:
                append(newInterval[0], newInterval[1])
                used = True
            append(s,e)
        if not used:
            append(newInterval[0], newInterval[1])
        return out

