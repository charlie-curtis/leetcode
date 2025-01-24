class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        m,n = len(grid), len(grid[0])
        
        seen = set()
        def dfs(i,j, prev):
            #print(i,j)
            if i < 0 or j < 0 or i == m or j == n:
                return False

            if (i,j, prev) in seen:
                return False
            seen.add((i,j, prev))
                
            if i == m-1 and j == n-1:
                return True
            
            if grid[i][j] == 1:
                a = dfs(i, j+1, grid[i][j]) if (j+1 < n and grid[i][j+1] in [1,3,5]) else False
                b = dfs(i, j-1, grid[i][j]) if (j-1 >= 0 and grid[i][j-1] in [1,4,6]) else False
            if grid[i][j] == 2:
                a = dfs(i-1, j, grid[i][j]) if (i-1 >=0 and grid[i-1][j] in [2,3,4]) else False
                b = dfs(i+1, j, grid[i][j]) if (i+1 < m and grid[i+1][j] in [2,5,6]) else False
            if grid[i][j] == 3:
                a = dfs(i, j-1, grid[i][j]) if (j-1 >= 0 and grid[i][j-1] in [1,4,6]) else False
                b = dfs(i+1, j, grid[i][j]) if (i+1 < m and grid[i+1][j] in [2,5,6]) else False
            if grid[i][j] == 4:
                a = dfs(i, j+1, grid[i][j]) if (j+1 < n and grid[i][j+1] in [1,3,5]) else False
                b = dfs(i+1, j, grid[i][j]) if (i+1 < m and grid[i+1][j] in [2,5,6]) else False
            if grid[i][j] == 5:
                a = dfs(i, j-1, grid[i][j]) if (j-1 >=0 and grid[i][j-1] in [1,4,6]) else False
                b = dfs(i-1, j, grid[i][j]) if (i-1 >=0 and grid[i-1][j] in [2,3,4]) else False
            if grid[i][j] == 6:
                a = dfs(i, j+1, grid[i][j]) if (j+1 < n and grid[i][j+1] in [1,3,5]) else False
                b = dfs(i-1, j, grid[i][j]) if (i-1 >= 0 and grid[i-1][j] in [2,3,4]) else False

            return a or b

        return dfs(0,0,-1)