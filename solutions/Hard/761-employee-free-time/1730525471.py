"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        pq = []
        n = len(schedule)
        pq = []

        #enqueue the first elements
        for i in range(n):
            start,end = schedule[i][0].start, schedule[i][0].end
            pq.append([start, 1, i, 0])
            pq.append([end, -1, i, 0])

        heapq.heapify(pq)

        cur =0
        beg = -1
        ans = []
        while pq:
            time = pq[0][0]
            requeue = []
            while pq and pq[0][0] == time:
                _, diff, i, j= heapq.heappop(pq)
                requeue.append([i,j, diff])
                cur+=diff

            if cur == 0 and beg == -1:
                beg = time
            elif cur > 0 and beg != -1:
                ans.append(Interval(beg, time))
                beg = -1

            for i,j,diff in requeue:
                j+=1
                if j < len(schedule[i]):
                    start,end = schedule[i][j].start, schedule[i][j].end
                    if diff == 1:
                        heapq.heappush(pq, [start, 1, i, j])
                    else:
                        heapq.heappush(pq, [end, -1, i, j])

        return ans