class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        pq = []
        ans = 0
        def pick(i):
            expire, amt = heapq.heappop(pq)
            if expire <= i:
                return 0
            amt-=1
            if amt > 0:
                heapq.heappush(pq, [expire, amt])
            return 1

        for i,(a,t) in enumerate(zip(apples, days)):
            if a > 0 and t > 0:
                heapq.heappush(pq, [i+t, a])
            while pq:
                res = pick(i)
                if not res:
                    continue
                ans+=1
                #we picked one for this date
                break
        i = len(apples) 
        while pq:
            res = pick(i)
            if not res:
                continue
            ans+=1
            i+=1
        return ans