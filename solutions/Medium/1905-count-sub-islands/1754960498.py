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
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        #do a DSU of grid1
        #do a DSU of grid2
        #iterate over grid2. For all roots in grid2 (where cell = 1), correlate it with a root from grid1 (where cell = 1). Then, iterate over all the roots in grid2. If there is exactly 1 root found in grid1, then we can increment our answer
        def connect(g):
            m,n = len(g), len(g[0])
            dsu = DisjointSetUnion(m*n)
            for i in range(m):
                for j in range(n):
                    if g[i][j] != 1:
                        continue
                    dirs = [[-1,0], [1,0], [0,1], [0,-1]]
                    for x,y in dirs:
                        ni,nj = i+x, j +y
                        if min(ni,nj) >= 0 and ni < m and nj < n and g[ni][nj] == 1:
                            dsu.union(i*n + j, ni*n + nj)
            return dsu

        H = defaultdict(set)
        dsu1 = connect(grid1)
        dsu2 = connect(grid2)

        m,n = len(grid2),len(grid2[0])
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    r = dsu2.find(i*n + j)
                    if grid1[i][j] == 0:
                        H[r].add(-1)
                    else:
                        H[r].add(dsu1.find(i*n+j))
        ans = 0
        for st in H.values():
            if len(st) == 1 and -1 not in st:
                ans+=1
        return ans




        