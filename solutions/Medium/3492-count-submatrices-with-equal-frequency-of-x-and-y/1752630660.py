class Solution:
    def numberOfSubmatrices(self, g: List[List[str]]) -> int:

        m, n = len(g), len(g[0])

        preX = [[0 for _ in range(n+1)] for _ in range(m+1)]
        preY = [[0 for _ in range(n+1)] for _ in range(m+1)]

        ans = 0
        for i in range(m):
            for j in range(n):
                preX[i+1][j+1] = preX[i+1][j] + preX[i][j+1] - preX[i][j]
                preY[i+1][j+1] = preY[i+1][j] + preY[i][j+1] - preY[i][j]

                if g[i][j] == 'X':
                    preX[i+1][j+1]+=1
                elif g[i][j] == 'Y':
                    preY[i+1][j+1]+=1
                
                if preX[i+1][j+1] == preY[i+1][j+1] and preX[i+1][j+1] > 0:
                    ans+=1
        return ans

        