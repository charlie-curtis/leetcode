class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        best = 0
        def dfs(i,j, seen):
            if i < 0 or j < 0 or i == m or j == n:
                return 0
            if (i,j) in seen or grid[i][j] == 0:
                return 0
            
            seen.add((i,j))
            dests = [[i+1,j], [i-1, j], [i, j+1], [i, j-1]]
            ans = grid[i][j]
            for ni, nj in dests:
                ans = max(ans, dfs(ni,nj, seen) + grid[i][j])
            seen.remove((i,j))
            return ans


        for i in range(m):
            for j in range(n):
                best = max(best, dfs(i,j, set()))
        return best
        