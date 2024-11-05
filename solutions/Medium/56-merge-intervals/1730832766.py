class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        out = []
        cur = intervals[0]

        for start,end in intervals[1:]:
            if start<= cur[1]:
                cur[1] = max(end, cur[1])
            else:
                out.append(cur.copy())
                cur = [start,end]
        out.append(cur)
        return out
        