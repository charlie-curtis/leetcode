class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:


        m,n = len(s1), len(s2)
        @cache
        def dp(i,j):
            if i == m and j == n:
                return 0
            if i == m:
                return dp(i, j+1) + ord(s2[j])
            if j == n:
                return dp(i+1, j) + ord(s1[i])
            
            if s1[i] == s2[j]:
                return dp(i+1, j+1)
            a = dp(i, j+1) + ord(s2[j])
            b = dp(i+1, j) + ord(s1[i])
            return min(a,b)

        return dp(0,0)

        