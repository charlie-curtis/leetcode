class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m,n = len(mat), len(mat[0])

        ROW_SIGNAL = 1.5
        COL_SIGNAL = 2.5
        BOTH_SIGNAL = 3.5
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    if mat[i][0] in [ROW_SIGNAL, BOTH_SIGNAL]:
                        mat[i][0] = BOTH_SIGNAL
                    else:
                        mat[i][0] = COL_SIGNAL
                    if mat[0][j] in [COL_SIGNAL, BOTH_SIGNAL]:
                        mat[0][j] = BOTH_SIGNAL
                    else:
                        mat[0][j] = ROW_SIGNAL
        
        print(mat)
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1, -1):
                if mat[i][0] in [COL_SIGNAL, BOTH_SIGNAL] or mat[0][j] in [ROW_SIGNAL, BOTH_SIGNAL]:
                    mat[i][j] = 0