class Solution:
    def getFood(self, grid: List[List[str]]) -> int:


        q = deque()
        seen = set()
        m,n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append([i,j, 0])
                    seen.add((i,j))
                    break

        while q:

            i,j,cost = q.popleft()

            dirs = [[-1, 0], [1,0], [0, -1], [0,1]]

            for x,y in dirs:
                nx, ny = i+x, j+y
                if nx < 0 or ny < 0 or nx == m or ny == n:
                    continue
                if (nx,ny) in seen:
                    continue
                if grid[nx][ny] == '#':
                    return cost+1
                if grid[nx][ny] == 'O':
                    q.append([nx,ny, cost+1])
                seen.add((nx,ny))

        return -1