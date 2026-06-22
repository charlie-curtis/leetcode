class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        ans = 0
        for j in range(n):
            for i in range(1,m):
                a = grid[i][j]
                b = grid[i-1][j]
                if a <= b:
                    ans+=abs(a-b)+1
                    grid[i][j] = grid[i-1][j]+1
        return ans
                
        