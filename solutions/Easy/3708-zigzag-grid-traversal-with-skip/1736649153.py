class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:

        m,n = len(grid), len(grid[0])

        skip = False
        out = []
        for i in range(m):
            if i % 2 == 0:
                for j in range(n):
                    if not skip:
                        out.append(grid[i][j])
                    skip = not skip
            else:
                for j in range(n-1, -1, -1):
                    if not skip:
                        out.append(grid[i][j])
                    skip = not skip
        return out
                    
        