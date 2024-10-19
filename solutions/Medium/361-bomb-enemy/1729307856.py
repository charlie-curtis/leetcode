class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:

        m,n = len(grid), len(grid[0])

        counts = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            cnt = 0
            for j in range(n):
                if grid[i][j] == 'W':
                    cnt = 0
                elif grid[i][j] == 'E':
                    cnt+=1
                else:
                    counts[i][j]+=cnt

        for i in range(m):
            cnt = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 'W':
                    cnt = 0
                elif grid[i][j] == 'E':
                    cnt+=1
                else:
                    counts[i][j]+=cnt

        for j in range(n):
            cnt = 0
            for i in range(m):
                if grid[i][j] == 'W':
                    cnt = 0
                elif grid[i][j] == 'E':
                    cnt+=1
                else:
                    counts[i][j]+=cnt

        for j in range(n):
            cnt = 0
            for i in range(m-1, -1, -1):
                if grid[i][j] == 'W':
                    cnt = 0
                elif grid[i][j] == 'E':
                    cnt+=1
                else:
                    counts[i][j]+=cnt

        best = 0
        for i in range(m):
            for j in range(n):
                best = max(best, counts[i][j])
        return best