class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:

        m,n = len(grid), len(grid[0])
        @cache
        def dp(i,j, b):

            if i < 0 or j < 0 or i == m or j == n:
                return False
            
            b+=1 if grid[i][j] == 1 else -1
            if i == m-1 and j == n-1:
                return b == 0

            return dp(i+1, j, b) or dp(i, j+1, b)


        return dp(0,0,0)
        