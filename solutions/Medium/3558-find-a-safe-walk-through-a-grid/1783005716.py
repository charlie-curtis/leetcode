class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        q = deque()
        n,m = len(grid), len(grid[0])
        health-=grid[0][0]
        q.append([0,0, health])

        visited = [[-1 for _ in range(m)] for _ in range(n)]
        visited[0][0] = health

        while q:
            i,j,cur_health = q.popleft()

            if i == n-1 and j == m-1:
                return True


            dirs = [[-1,0], [1,0], [0,1], [0,-1]]
            for x,y in dirs:
                if i+x < 0 or i+x >= n or j+y < 0 or j+y >= m:
                    continue
                tmp_health = cur_health-grid[i+x][j+y]

                if tmp_health <= 0:
                    continue
                if visited[i+x][j+y] >= tmp_health:
                    continue
                visited[i+x][j+y] = tmp_health 

                q.append([i+x, j+y, tmp_health])
                
        return False


        