class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        C=Counter(tasks)
        h = []
        cur=[]
        for v in C.values():
            heapq.heappush(h,[0,-v])
        
        t=0
        while h or cur:
            while h and h[0][0] <= t:
                heapq.heappush(cur, heapq.heappop(h)[1])
            if not cur:
                t=h[0][0]
                continue
            
            v = heapq.heappop(cur)
            v=-v
            t+=1
            v-=1
            if v:
                heapq.heappush(h, [t+n, -v])
        return t
        
            