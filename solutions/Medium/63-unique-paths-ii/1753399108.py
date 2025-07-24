class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        if grid[m-1][n-1] == 1:
            return 0

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                dp[i+1][j]+= dp[i][j]
                dp[i][j+1]+= dp[i][j]
        return dp[m-1][n-1]