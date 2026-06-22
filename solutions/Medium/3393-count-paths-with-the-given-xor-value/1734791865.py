class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:


        m,n = len(grid), len(grid[0])
        M = 10**9 + 7
        @cache
        def dp(i,j, cur):

            if i < 0 or j < 0 or i == m or j == n:
                return 0

            if i == m-1 and j == n -1:
                if cur^grid[i][j] == k:
                    return 1
                return 0

            a = dp(i+1, j, cur^grid[i][j]) % M
            b = dp(i, j+1, cur^grid[i][j]) % M

            return (a+b) % M

        return dp(0,0, 0)

            
        