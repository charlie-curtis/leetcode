class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        li = SortedDict()
        for i, (x,y) in enumerate(intervals):
            li[x] = i

        out = []
        for start,end in intervals:
            idx = li.bisect_left(end)
            if idx < len(li):
                out.append(li.peekitem(idx)[1])
            else:
                out.append(-1)
        return out