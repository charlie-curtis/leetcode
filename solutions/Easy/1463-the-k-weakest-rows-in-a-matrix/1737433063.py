class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        A = []
        m,n = len(mat), len(mat[0])
        for i in range(m):
            cnt = 0
            for j in range(n):
                if mat[i][j] == 1:
                    cnt+=1
            A.append((cnt,i))

        A.sort()
        out = []
        for i in range(k):
            out.append(A[i][1])
        return out
            
                
        