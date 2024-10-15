class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:

        m,n = len(mat), len(mat[0])
        anti_diags = [[0 for _ in range(n)] for _ in range(m)]
        diags = [[0 for _ in range(n)] for _ in range(m)]
        lefts = [[0 for _ in range(n)] for _ in range(m)]
        ups = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                anti_diags[i][j] = 1
                diags[i][j] = 1
                lefts[i][j] = 1
                ups[i][j] = 1
                if i > 0 and j > 0:
                    diags[i][j]+=diags[i-1][j-1]
                if j > 0:
                    lefts[i][j]+= lefts[i][j-1]
                if i > 0:
                    ups[i][j]+= ups[i-1][j]
                if i-1 >= 0 and j + 1 < n:
                    anti_diags[i][j]+= anti_diags[i-1][j+1]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, diags[i][j], ups[i][j], lefts[i][j], anti_diags[i][j])
        return ans

        