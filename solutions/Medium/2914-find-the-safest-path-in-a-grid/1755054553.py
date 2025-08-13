class Solution:
    def maximumSafenessFactor(self, g: List[List[int]]) -> int:



        q = []
        m,n = len(g), len(g[0])

        dsts = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    q.append([i,j])
                    dsts[i][j] = 0
        


        d = 1
        while q:
            tmp = []
            for _ in range(len(q)):
                    i,j = q.pop()
                    dirs = [[-1,0], [1,0], [0,1], [0,-1]]
                    for x,y in dirs:
                        ni,nj = x+i, y+j
                        if min(ni,nj) >= 0 and ni < m and nj < n and dsts[ni][nj] == -1:
                            dsts[ni][nj] = d
                            tmp.append([ni,nj])
            q = tmp
            d+=1

        l = 0
        r = m*n

        def dfs(i,j, mid, V):
            if min(i,j) < 0 or i == m or j == n or V[i][j] or dsts[i][j] < mid:
                return False
            if i == m-1 and j == n-1:
                return True
            V[i][j] = True
            return any([
                dfs(i+1, j, mid, V),
                dfs(i, j+1, mid, V),
                dfs(i-1, j, mid, V),
                dfs(i, j-1, mid, V)
            ])

        def check(mid):
            V = [[False for _ in range(n)] for _ in range(m)]

            return dfs(0,0, mid, V)


        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r