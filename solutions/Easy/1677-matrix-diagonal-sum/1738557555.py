class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        ssum = 0
        m,n = len(mat), len(mat[0])

        ssum=0
        for i in range(m):
            for j in range(n):
                if i == j or (i+j == n-1):
                    print("including", mat[i][j])
                    ssum+=mat[i][j]
        return ssum
        