class Solution:
    def minDistance(self, s: str, t: str) -> int:


        m,n = len(s), len(t)
        @cache
        def dp(i,j):
            if i == m or j == n:
                return m-i + n-j
            
            if s[i] == t[j]:
                return dp(i+1, j+1)
            return min(dp(i+1, j), dp(i,j+1)) +1 
        return dp(0,0)
        