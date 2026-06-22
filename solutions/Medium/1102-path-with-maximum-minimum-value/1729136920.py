class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        def check(val):

            if grid[m-1][n-1] < val:
                return False

            def dfs(i,j, seen, val):
                if i == m-1 and j == n-1: return True
                
                if i < 0 or j < 0 or i == m or j == n: return False
                if (i,j) in seen: return False
                if grid[i][j] < val: return False

                seen.add((i,j))
                a = dfs(i-1, j, seen, val)
                b = dfs(i+1, j, seen, val)
                c = dfs(i, j+1, seen, val)
                d = dfs(i, j-1, seen, val)

                return a or b or c or d

            return dfs(0,0,set(), val)

        l = 0
        r = 10**9

        #TTTTTTTFFFFF
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid +1
            else:
                r = mid -1
        return r