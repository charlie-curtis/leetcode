class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def matrixRankTransform(self, grid: List[List[int]]) -> List[List[int]]:

        m,n = len(grid), len(grid[0])

        dsu = DisjointSetUnion(m*n)

        rowV = {}
        colV = {}
        seen = []
        for i in range(m):
            for j in range(n):
                seen.append([grid[i][j], i,j])
                rowkey = (i,grid[i][j])
                if rowkey in rowV:
                    x,y = rowV[rowkey]
                    u,v = i*n + j, x*n + y
                    dsu.union(u,v)
                else:
                    rowV[rowkey] = (i,j)
                colkey = (j,grid[i][j])
                if colkey in colV:
                    x,y = colV[colkey]
                    u,v = i*n + j, x*n + y
                    dsu.union(u,v)
                else:
                    colV[colkey] = (i,j)


        seen = [(grid[i][j], dsu.find(i*n + j), i, j) for _, i,j in seen]
        seen.sort()

        out = [[0]*n for _ in range(m)]
        rows = [0]*m
        cols = [0]*n
            

        cur = 0
        while cur < len(seen):

            rank = 1
            idxs = []
            root = seen[cur][1]
            while cur < len(seen) and seen[cur][1] == root:
                row, col = seen[cur][2], seen[cur][3]
                idxs.append((row,col))
                rank = max(rows[row]+1, rank)
                rank = max(cols[col]+1, rank)
                cur+=1
            for i,j in idxs:
                out[i][j] = rank
                rows[i] = rank
                cols[j] = rank
        return out
                           
