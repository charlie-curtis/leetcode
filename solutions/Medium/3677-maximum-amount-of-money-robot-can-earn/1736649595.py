class Solution:
    def maximumAmount(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        @cache
        def dp(i,j, rem):
            if rem < 0:
                return -1e15
            if (i == m-1 and j == n) or (i ==m and j == n-1):
                return 0

            if i == m or j == n:
                return -1e15

            
            options = [-1e15]
            if grid[i][j] < 0:
                #don't steal anything, but use rem
                a = dp(i+1, j, rem-1)
                b = dp(i, j+1, rem-1)
                options.append(a)
                options.append(b)

                a = dp(i+1, j, rem) - abs(grid[i][j])
                b = dp(i, j+1, rem) - abs(grid[i][j])

                options.append(a)
                options.append(b)
            else:
                a = dp(i+1, j, rem) + grid[i][j]
                b = dp(i, j+1, rem) + grid[i][j]
                options.append(a)
                options.append(b)

            return max(options)

        return dp(0,0,2)
                
                
                
                
                
                
        