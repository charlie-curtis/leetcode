class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:


        m,n = len(mat), len(mat[0])
        C = Counter()
        for i in range(m):
            for j in range(n):
                if j == 0 or mat[i][j-1] != mat[i][j]:
                    C[mat[i][j]]+=1


        
        ans = float('inf')
        for k,v in C.items():
            if v == m:
                ans = min(ans, k)

        return ans if ans != float('inf') else -1
        