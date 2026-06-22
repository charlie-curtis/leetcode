class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:


        n = len(grid)
        @cache
        def dp(i, avoid):
            if i == n:
                return 0
            
            best = min([dp(i+1,j) + grid[i][j] for j in range(n) if j != avoid])
            return best

        return dp(0, -1)
        