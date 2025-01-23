class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:


        pq = []

        A = list(zip(efficiency, speed))
        A.sort(reverse=True)

        ssum = 0
        ans = 0
        for e,s in A:

            heappush(pq,s)
            ssum+=s
            if len(pq) > k:
                ssum-=heappop(pq)

            ans = max(e*ssum, ans)

        return ans % (10**9 + 7)
                
        
        