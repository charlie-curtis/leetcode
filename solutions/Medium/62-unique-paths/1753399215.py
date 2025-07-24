class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i+1][j]+=dp[i][j]
                dp[i][j+1]+=dp[i][j]
        return dp[m-1][n-1]