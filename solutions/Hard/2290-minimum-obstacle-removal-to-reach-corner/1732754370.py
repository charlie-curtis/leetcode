class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])


        INF = 10**9
        dst = [[INF for _ in range(n)] for _ in range(m)]
        q = deque() 
        q.append((grid[0][0], 0, 0))
        dst[0][0] = grid[0][0]

        while q:

            cost,i,j = q.popleft()

            if dst[i][j] < cost:
                continue

            new_cost= cost + grid[i][j]
            if i == m-1 and j == n-1:
                return new_cost 

            dirs = [[-1,0], [1,0], [0,1], [0,-1]]
            neighbors = ((i+x, j+y) for x,y in dirs)

            for x,y in neighbors:
                if x < 0 or y < 0 or x == m or y == n or dst[x][y] <= new_cost:
                    continue
                dst[x][y] = new_cost

                #this is the only modification from dijkstra. This is 0/1 BFS. If the grid we reached is "free",then we can put it in the front of our queue
                if new_cost > cost:
                    q.append((new_cost, x,y))
                else:
                    q.appendleft((new_cost, x,y ))

        return -1
                    
