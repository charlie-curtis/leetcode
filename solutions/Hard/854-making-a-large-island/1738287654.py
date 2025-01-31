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
    def largestIsland(self, grid: List[List[int]]) -> int:


        m, n = len(grid) , len(grid[0])
        dsu = DisjointSetUnion(n*m)

        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                nxt = [(i+x,j+y) for (x,y) in dirs]
                for x,y in nxt:
                    if min(x,y) < 0 or x == m or y == n:
                        continue
                    if grid[x][y] == 1:
                        dsu.union(i*n + j, x*n + y)
                    
        best = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    best = max(best, dsu.set_size(i*n + j))
                    continue
                nxt = [(i+x,j+y) for (x,y) in dirs]
                roots = set()
                for x,y in nxt:
                    if min(x,y) < 0 or x == m or y == n:
                        continue
                    if grid[x][y] == 1:
                        roots.add(dsu.find(x*n + y))
                
                ssum = 1  
                for r in roots:
                    ssum+=dsu.set_size(r)
                best = max(ssum, best)
        return best
        