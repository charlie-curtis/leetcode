class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:


        d = defaultdict(list)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                d[j-i].append(grid[i][j])

        for k,li in d.items():
            if k <= 0:
                d[k] = deque(sorted(li)[::-1])
            else:
                d[k] = deque(sorted(li))



        out = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                out[i][j] = d[j-i].popleft()
        return out
        