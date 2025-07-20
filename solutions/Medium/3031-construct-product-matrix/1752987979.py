class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        m,n = len(grid), len(grid[0])

        if m*n == 1:
            return [[0]]
    
        MOD =12345
        
        pre = [0]*(m*n)
        suf = [0]*(m*n)
        out = [[0 for _ in range(n)] for _ in range(m)]
    
        cur = 1
        for i in range(m):
            for j in range(n):
                v = i*n + j
                cur*=grid[i][j]
                cur%=MOD
                pre[v] = cur

        cur = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                v = i*n + j
                cur*=grid[i][j]
                cur%=MOD
                suf[v] = cur
        
        for i in range(m):
            for j in range(n):
                v = i*n + j
                if v == 0:
                    out[i][j] = suf[1]
                elif v == m*n -1:
                    out[i][j] = pre[-2]
                else:
                    out[i][j] = (pre[v-1]*suf[v+1]) % MOD

        return out

        