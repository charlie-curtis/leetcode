class Solution:
    def diagonalSort(self, grid: List[List[int]]) -> List[List[int]]:

        m,n = len(grid), len(grid[0])

        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                #what row is it in when j = 0
                d[i-j].append(grid[i][j])


        for k,li in d.items():
            d[k] = sorted(li, reverse=True)

        out = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                out[i][j] = d[i-j].pop()
        return out

        