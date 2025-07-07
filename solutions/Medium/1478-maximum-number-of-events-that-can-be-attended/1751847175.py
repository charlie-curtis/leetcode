class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        d = defaultdict(list)
        M = 0
        for start,end in events:
            M = max(M, end)
            d[start].append(end)

        pq = []
        ans = 0
        for x in range(M+1):
            for y in d[x]:
                heapq.heappush(pq, y)
            while pq and pq[0] < x:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans+=1
        return ans


        
