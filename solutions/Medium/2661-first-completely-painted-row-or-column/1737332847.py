class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        m,n = len(mat), len(mat[0])
        d = {}
        for i in range(m):
            for j in range(n):
                x = mat[i][j]
                d[x] = (i,j)

        rows = [0]*m
        cols = [0]*n
        for k,x in enumerate(arr):
            i,j = d[x]
            rows[i]+=1
            cols[j]+=1
            if rows[i] == n or cols[j] == m:
                return k

        raise ValueError("Wrong")
        