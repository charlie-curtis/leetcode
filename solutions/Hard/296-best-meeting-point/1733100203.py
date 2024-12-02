class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:



        #I solved this problem 3 ways
        #1. original solution was snaking my way through the 2d grid. Compute the initial score for (0,0) then compute the delta for each cell as you
        #snake through

        #2. same thing, but treat the problem as 2 independent arrays instead of a 2D grid (thanks editorial)

        #3. treat as 2 independent problems, but use the median

        m,n = len(grid), len(grid[0])

        rows = []
        cols = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        base = [median(rows), median(cols)] #could also sort and do something similar with special handling of even length arrays

        score = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:

                    score+=abs(i-base[0])
                    score+=abs(j-base[1])
        return int(score)

