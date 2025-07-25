class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        g=grid
        m,n= len(g),len(g[0])
        def dfs(i,j,seen):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] == 0 or (i,j) in seen:
                return
            seen.add((i,j))
            dfs(i+1,j,seen)
            dfs(i-1,j,seen)
            dfs(i,j-1,seen)
            dfs(i,j+1,seen)

        overall = set()
        ans=0
        for i in range(m):
            for j in range(n):
                if g[i][j]==1 and (i,j) not in overall:
                    st = set()
                    dfs(i,j,st)
                    ans=max(ans,len(st))
                    overall.update(st)
        return ans
        