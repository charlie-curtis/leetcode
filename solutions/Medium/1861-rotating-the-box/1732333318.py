class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:

        m,n = len(grid), len(grid[0])

        out = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                out[j][m-1-i] = grid[i][j]

        m,n = len(out), len(out[0])
        for j in range(n):

            bottom_ptr = -1
            for i in range(m-1, -1, -1):
                if out[i][j] == '*':
                    bottom_ptr = -1
                elif out[i][j] == '.':
                    #this is a free spot.
                    if bottom_ptr == -1:
                        bottom_ptr = i
                else:
                    if bottom_ptr != -1:
                        out[bottom_ptr][j], out[i][j] = out[i][j], out[bottom_ptr][j]
                        bottom_ptr-=1

        return out