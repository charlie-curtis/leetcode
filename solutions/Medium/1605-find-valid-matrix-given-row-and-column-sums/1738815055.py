class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:


        m, n = len(rowSum), len(colSum)


        rows = []
        for i,x in enumerate(rowSum):
            if x != 0:
                rows.append([x,i])
        cols = []
        for i,x in enumerate(colSum):
            if x != 0:
                cols.append([x,i])

        heapify(cols)
        heapify(rows)


        out = [[0 for _ in range(n)] for _ in range(m)]
        while len(rows):
            v,i = heappop(rows)
            v2,j= heappop(cols)
            #print(i,j,m,n)
            out[i][j] = min(v,v2)
            if v == v2:
                continue
            if v2 > v:
                heappush(cols, [v2-v,j])
            else:
                heappush(rows, [v-v2, i])
        return out
            