class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        ans = 0
        for L in range(1,n+1):
            for i in range(0,n-L+1):
                j = i+L-1
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                ans = max(ans, dp[i][j])

        return ans


        