class Solution:
    def minTimeToReach(self, time: List[List[int]]) -> int:


        m,n = len(time), len(time[0])
        pq = [[0,0,0,0]]

        dst = {}
        while pq:
            cost, i,j, cnt = heapq.heappop(pq)
            cnt%=2

            if i == m-1 and j == n -1:
                return cost

            dirs = [[-1,0], [1,0], [0,1], [0,-1]]
            nxt = [[i+a, j+b] for a,b in dirs]

            for ni,nj in nxt:
                if ni < m and nj < n and min(ni,nj) >= 0:
                    newcost = max(cost + cnt+1, (time[ni][nj] + cnt+1))
                    if (ni, nj, cnt+1) not in dst or dst[(ni,nj, cnt+1)] > newcost:
                        dst[(ni,nj,cnt+1)] = newcost
                        heapq.heappush(pq, [newcost, ni, nj, cnt+1])