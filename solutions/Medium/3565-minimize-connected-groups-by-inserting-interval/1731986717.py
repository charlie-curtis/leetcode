class Solution:
    def minConnectedGroups(self, intervals: List[List[int]], k: int) -> int:

        intervals.sort()

        new = []
        for start,end in intervals:
            if not new or new[-1][1] < start:
                new.append([start,end])
            else:
                #we can merge this interval
                end = max(end, new[-1][1])
                new[-1] = [new[-1][0], end]


        n = len(new)
        d = []
        ans = n
        for i in range(n):
            start,end = new[i]
            d.append(end)
            j = bisect_left(d, start - k)
            ans = min(ans, n-(i-j))

        return ans