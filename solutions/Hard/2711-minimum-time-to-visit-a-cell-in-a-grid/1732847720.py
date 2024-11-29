class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:


        m,n = len(grid), len(grid[0])

        INF = 10**9
        pq = [[0,0, 0]]
        dst = [[INF for _ in range(n)] for _ in range(m)]
        dst[0][0] = 0

        if m == 1 and n == 1:
            return 0
        has_move = (m > 1 and grid[1][0] <= 1) or (n > 1 and grid[0][1] <= 1)

        if not has_move:
            return -1

        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        #need to handle the test case where the path itself is longer than the values at grid[i][j]. Aka the path is the bottleneck
        while pq:
            score, i,j = heapq.heappop(pq)

            if dst[i][j] < score:
                #stale
                continue

            neighbors = [(i+x, j+y) for (x,y) in dirs]

            for x,y in neighbors:
                if x < 0 or y < 0 or x == m or y == n:
                    continue
                
                if score >= grid[x][y]:
                    #by the tiem we got to grid[i][j], enough time has elapsed that we can move directly into the cell
                    can_score = score + 1
                else:
                    #not enough time has elapsed, so we need to "waste" time by alternating btwn the last 2 cells. We can time it
                    #up so that we either land on cell (i,j) right at t= grid[i][j] OR we land on cell (i,j) at t = grid[i][j]+1
                    can_score = grid[x][y] if ((grid[x][y] - score) % 2 == 1) else grid[x][y] + 1
                if x == m-1 and y == n-1:
                    return can_score
                if can_score < dst[x][y]:
                    heapq.heappush(pq,(can_score,x,y))
                    dst[x][y] = can_score

        return -1 if dst[m-1][n-1] == INF else dst[m-1][n-1]


