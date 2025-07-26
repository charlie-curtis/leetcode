class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        g = grid

        for i in range(m):
            g[i] = sorted(grid[i])

        end = (1<<m) -1
        @cache
        def dp(x, mask):
            if mask == end:
                return 0

            best = 0
            for i in range(m):
                if (mask&(1<<i)) == 0:
                    idx = bisect_right(g[i], x) - 1
                    if idx >= 0:
                        best = max(best, g[i][idx] + dp(g[i][idx]-1, mask|(1<<i)))
            return best
        
        return dp(100, 0)
