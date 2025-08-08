class Solution:
    def highestPeak(self, g: List[List[int]]) -> List[List[int]]:

        m,n = len(g), len(g[0])

        out = [[-2 for _ in range(n)] for _ in range(m)]

        q = []
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    out[i][j] = 0
                    q.append([i,j])

        dst = 0
        while q:
            tmp = []
            for _ in range(len(q)):
                i,j = q.pop()
                out[i][j] = dst
                nxt = [[-1,0], [1,0], [0,1], [0,-1]]
                for ni, nj in nxt:
                    x,y = i + ni, j + nj
                    if x >= 0 and y >= 0 and x < m and y < n and out[x][y] == -2:
                        tmp.append([x,y])
                        out[x][y] = -1
            dst+=1
            q = tmp
        return out