class Solution:
    def minInsertions(self, s: str) -> int:

        n = len(s)
        @cache
        def dp(i,j):
            if i >= j:
                return 0


            if s[i] == s[j]:
                return dp(i+1, j-1)
            else:
                a = 1 + dp(i+1, j)
                b = 1 + dp(i, j-1)
                return min(a,b)
        return dp(0, n-1)