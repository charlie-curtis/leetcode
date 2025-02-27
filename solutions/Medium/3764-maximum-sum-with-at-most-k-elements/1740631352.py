class Solution:
    def maxSum(self, g: List[List[int]], limits: List[int], k: int) -> int:

        m,n=len(g),len(g[0])

        pq = []
        for i in range(m):
            for j in range(n):
                pq.append([-g[i][j], i])
        ans=0
        heapify(pq)
        while k > 0 and len(pq) > 0:
            v,i = heappop(pq)
            if limits[i] > 0:
                ans+=-v
                limits[i]-=1
                k-=1
        return ans

        