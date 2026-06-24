class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])


        @cache
        def f(x,y):
            if x >= m or y >= n:
                return 10**9
            if x == m-1 and y == n-1:
                return grid[x][y]
            
            return min(f(x+1,y), f(x,y+1)) + grid[x][y]

        
        return f(0,0)
            
        