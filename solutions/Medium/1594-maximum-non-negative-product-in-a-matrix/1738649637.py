class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        INF = 10**9

        m,n = len(grid), len(grid[0])
        @cache
        def dp(i,j):
            if i < 0 or j < 0 or i == m or j == n:
                return [INF, INF]

            if i == m-1 and j == n-1:
                return [grid[i][j], grid[i][j]]


            a = dp(i+1,j)
            b = dp(i, j+1)

            eligible = set()
            for x in a+b:
                if x != INF:
                    eligible.add(x)


            if not eligible:
                return [INF, INF]

            mmin = min([grid[i][j]*x for x in eligible])
            mmax= max([grid[i][j]*x for x in eligible])

            return [mmin, mmax]


        res = dp(0,0)
        print(res)
        if res[1] < 0:
            return -1
        return res[1] % (10**9 + 7)
        