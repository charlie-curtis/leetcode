class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        def bt(i,j, rows_rem, cols_rem):
            if j == n:
                return bt(i+1, 0, rows_rem, cols_rem)
            
            if i == m:
                for i in range(m):
                    for j in range(n):
                        bad = grid[i][j] == 1 and i in rows_rem and j in cols_rem
                        if bad:
                            return 1e10
                return 0
            
            #don't include it
            a = bt(i, j+1, rows_rem, cols_rem)
            b = 1e10

            #include it
            r = False
            c = False
            if i in rows_rem:
                rows_rem.remove(i)
                r = True
            if j in cols_rem:
                cols_rem.remove(j)
                c = True
            
            if grid[i][j] == 1:
                b = 1+ bt(i, j+1, rows_rem, cols_rem)
            if r:
                rows_rem.add(i)
            if c:
                cols_rem.add(j)

            return min(a,b)

        rows_rem = set()
        cols_rem = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows_rem.add(i)
                    cols_rem.add(j)
        return bt(0,0, rows_rem, cols_rem)