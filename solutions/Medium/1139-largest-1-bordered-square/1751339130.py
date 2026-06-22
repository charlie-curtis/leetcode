class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        lefts = [[0 for _ in range(n)] for _ in range(m)]
        ups = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            streak = 0
            for j in range(n):
                if grid[i][j] == 1:
                    streak+=1
                else:
                    streak = 0
                lefts[i][j] = streak
        
        for i in range(n):
            streak = 0
            for j in range(m):
                if grid[j][i] == 1:
                    streak+=1
                else:
                    streak = 0
                ups[j][i] = streak

        
        best = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                k = 1 
                while i-k+1 >=0 and j-k+1 >= 0:
                    if grid[i-k+1][j] == 0 or grid[i][j-k+1] == 0:
                        break
                    if lefts[i-k+1][j] >= k and ups[i][j-k+1] >= k:
                        best = max(best, k*k)
                    k+=1
        return best
