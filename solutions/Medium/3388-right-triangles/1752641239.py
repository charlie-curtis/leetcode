class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:

        R = Counter()
        C = Counter()

        m,n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    R[i]+=1
                    C[j]+=1

        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                a = max(R[i]-1,0)
                b = max(0,C[j]-1)

                ans+=a*b

        return ans
        