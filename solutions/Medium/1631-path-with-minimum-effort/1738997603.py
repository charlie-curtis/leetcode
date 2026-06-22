class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:


        l = 0
        r = 10**6 + 1

        def check(mid):

            seen = set()
            m,n = len(grid), len(grid[0])
            def dfs(i,j, prev):
                if min(i,j) < 0 or i == m or j == n:
                    return False
                if (i,j, prev) in seen:
                    return False
                if abs(grid[i][j] - prev) > mid:
                    return False

                if i == m-1 and j == n-1:
                    return True
                seen.add((i,j, prev))
                a = dfs(i+1, j, grid[i][j])
                if a:
                    return True
                b = dfs(i-1, j, grid[i][j])
                if b:
                    return True
                c = dfs(i, j+1, grid[i][j])
                if c:
                    return True
                d = dfs(i, j-1, grid[i][j])
                if d:
                    return True

                return False

            return dfs(0,0, grid[0][0])


        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l
        