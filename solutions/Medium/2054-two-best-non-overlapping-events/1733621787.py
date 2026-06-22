class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        #There is a common pattern where you can use a priority queue as a holding tank
        #I originally solved this using a sorted dictionary
        n = len(events)
        events.sort()
        mmax = 0
        pq = []

        ans = 0
        for start,end,v in events:
            while pq and pq[0][0] < start:
                mmax = max(mmax, heapq.heappop(pq)[1])
            
            ans = max(ans, v + mmax)
            heapq.heappush(pq, [end, v])
        return ans

        