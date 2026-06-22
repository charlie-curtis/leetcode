class Solution:
    def luckyNumbers(self, grid: List[List[int]]) -> List[int]:

        m,n = len(grid), len(grid[0])
        rows = {}
        cols = {}
        for i in range(m):
            for j in range(n):
                if i not in rows:
                    rows[i] = grid[i][j]
                else:
                    rows[i] = min(grid[i][j], rows[i])
                if j not in cols:
                    cols[j] = grid[i][j]
                else:
                    cols[j] = max(grid[i][j], cols[j])


        out = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == cols[j] and grid[i][j] == rows[i]:
                    out.append(grid[i][j])

        return out
                
        