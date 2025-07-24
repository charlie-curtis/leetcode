class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1), len(word2)
        dp=[[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n] = 0
        for i in range(m-1,-1,-1):
            dp[i][n] = dp[i+1][n] + 1
        for j in range(n-1, -1, -1):
            dp[m][j] = dp[m][j+1] + 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                good= word1[i] == word2[j]
                dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
                if good:
                    dp[i][j] = min(dp[i+1][j+1], dp[i][j])
        return dp[0][0]


'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m,n = len(word1), len(word2)

        @cache
        def dp(i,j):
            if i == m:
                return n-j
            if j == n:
                return m - i
            
            good = word1[i] == word2[j]
            if good:
                return dp(i+1,j+1)
            return min(dp(i+1,j), dp(i,j+1), dp(i+1,j+1)) + 1
        
        return dp(0,0)
'''