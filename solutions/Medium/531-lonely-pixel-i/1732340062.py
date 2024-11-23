class Solution:
    def findLonelyPixel(self, grid: List[List[str]]) -> int:

        m,n = len(grid), len(grid[0])

        row_count = Counter()
        col_count = Counter()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'B':
                    continue
                row_count[i]+=1
                col_count[j]+=1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'B':
                    continue
                if row_count[i] == col_count[j] == 1:
                    ans+=1
        return ans

        