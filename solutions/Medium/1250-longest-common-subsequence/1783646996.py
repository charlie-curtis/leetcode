class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:



        m,n = len(s1), len(s2)
        @cache
        def dp(i,j):
            if i == m or j == n:
                return 0
            
            if s1[i] == s2[j]:
                return 1 + dp(i+1, j+1)
            
            return max(
                dp(i+1,j),
                dp(i, j+1)
            )

        return dp(0,0)

        