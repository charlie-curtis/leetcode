class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        @cache
        def dp(i,j,k):

            if min(j,k) < 0 or max(k,j) == n:
                return -1e15
            if i == m:
                return 0

            options = []
            options.append(dp(i+1, j-1, k-1))
            options.append(dp(i+1, j, k-1))
            options.append(dp(i+1, j+1, k-1))
        
            options.append(dp(i+1, j-1, k))
            options.append(dp(i+1, j, k))
            options.append(dp(i+1, j+1, k))
            
            options.append(dp(i+1, j-1, k+1))
            options.append(dp(i+1, j, k+1))
            options.append(dp(i+1, j+1, k+1))


            other = grid[i][j] + grid[i][k]
            if j == k:
                other-=grid[i][j]

            return max(options) + other

        return dp(0, 0, n-1)