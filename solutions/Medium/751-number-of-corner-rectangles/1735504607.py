class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        C = Counter()

        def count(li):
            n = len(li)
            for i in range(n):
                for j in range(i+1,n):
                    a, b = li[i], li[j]
                    C[(a, b-a)]+=1
        for i in range(m):
            ones = []
            for j in range(n):
                if grid[i][j] == 1:
                    ones.append(j)
            count(ones)

        #O(M*N^2)

        #prior TLE was O(M^2*N^2)
        return sum([v*(v-1)//2 for v in C.values()])