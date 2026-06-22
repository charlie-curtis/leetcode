class Solution:
    def minTimeToReach(self, time: List[List[int]]) -> int:


        m,n = len(time), len(time[0])
        pq = [[0,0,0]]

        dst = {}
        while pq:
            cost, i,j = heapq.heappop(pq)

            if i == m-1 and j == n -1:
                return cost

            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            nxt = [[i+a, j+b] for a,b in dirs]
            for ni, nj in nxt:
                if ni < m and nj < n and min(ni,nj) >= 0:
                    newcost = max(cost + 1, (time[ni][nj] + 1))
                    if (ni,nj) not in dst or dst[(ni,nj)] > newcost:
                        dst[(ni,nj)] = newcost
                        heapq.heappush(pq, [newcost, ni, nj])