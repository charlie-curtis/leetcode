class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        INF = 10**9
        dsts = [[INF for _ in range(n)] for _ in range(m)]

        pq = [[0, m-1,n-1]]
        dsts[m-1][n-1] = 0
        while pq:

            cost, i,j = heapq.heappop(pq)

            if dsts[i][j] < cost:
                continue

            #1 = pointing right
            #2 = pointing left
            #3 = pointing down
            #4 = pointing up
            dirs = [[-1,0,3], [1,0, 4], [0,1,2], [0,-1,1]]
            nxt = [(x+i, y+j, d) for x,y,d in dirs]
            for ni, nj, d in nxt:
                if ni < 0 or nj < 0 or ni == m or nj == n:
                    continue
                newcost = cost + int(grid[ni][nj] != d)
                if dsts[ni][nj] > newcost:
                    dsts[ni][nj] = newcost
                    heapq.heappush(pq, [newcost, ni,nj])
        

        return dsts[0][0]


        