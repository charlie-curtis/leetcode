class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        smallx = largex = smally = largey = -1
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if smally == -1:
                        smally = i
                    largey = i
                    if smallx == -1 or j < smallx:
                        smallx = j
                    if largex == -1 or j > largex:
                        largex = j
        
        if smallx == -1:
            return 0
        return (largex - smallx + 1) * (largey - smally + 1)
        