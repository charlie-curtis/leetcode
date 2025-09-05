class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:


        MOD = 10**9  + 7
        @cache
        def dp(i,j, rem):
            if rem < 0:
                return 0
            if min(i,j) < 0 or i == m or j == n:
                return 1
            
            a = dp(i+1, j, rem-1)
            b = dp(i-1, j, rem-1)
            c = dp(i, j-1, rem-1)
            d = dp(i, j+1, rem-1)

            return (a+b+c+d) % MOD

        return dp(startRow, startColumn, maxMove)
        