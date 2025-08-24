class Solution:
    def numIslands(self, g: List[List[str]]) -> int:


        m,n = len(g), len(g[0])
        V = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i,j):
            if min(i,j) < 0 or i == m or j == n:
                return
            if V[i][j] or g[i][j] != '1':
                return
            
            V[i][j] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        
        ans = 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == '1' and not V[i][j]:
                    ans+=1
                    dfs(i,j)
        return ans
        