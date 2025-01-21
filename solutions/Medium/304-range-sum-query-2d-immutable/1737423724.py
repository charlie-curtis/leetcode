class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        m,n = len(mat), len(mat[0])
        self.m = m
        self.n = n
        self.pref = [[0 for _ in range(n+1)] for _ in range(m+1)]
        pref = self.pref
        for i in range(m):
            for j in range(n):
                a = pref[i+1][j]
                b = pref[i][j+1]
                c = pref[i][j]
                pref[i+1][j+1] = a + b - c + mat[i][j]
    def get(self,r, c):
        return self.pref[r+1][c+1]
    def queryByCorner(self,r1, c1, r2, c2):
        #r1, c1 (A)      #r1,c2 (B)


        #r2, c1 (C)     #r2,c2 (D)
        a = self.get(r1-1,c1-1)
        b = self.get(r1-1,c2)
        c = self.get(r2,c1-1)
        d = self.get(r2,c2)
        res = d + a - c - b
        return res


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.queryByCorner(row1,col1, row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)