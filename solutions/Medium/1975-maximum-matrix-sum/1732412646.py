class Solution:
    def maxMatrixSum(self, grid: List[List[int]]) -> int:

        V = []
        m,n = len(grid), len(grid[0])

        negs = 0
        zeros = 0
        for i in range(m):
            for j in range(n):
                g = grid[i][j]
                if g < 0:
                    negs+=1
                if g == 0:
                    zeros+=1
                V.append(abs(g))
        
        if negs % 2 == 0 or zeros > 0:
            return sum(V)

        return sum(V) - min(V)*2
        

        