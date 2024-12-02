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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:


        dsu = DisjointSetUnion(m*n)
        graph = [[0 for _ in range(n)] for _ in range(m)]

        out = []
        zeros = m*n
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        for i,j in positions:

            if graph[i][j] == 1:
                out.append(dsu.num_sets - zeros)
                continue
            
            zeros-=1
            graph[i][j] = 1

            for x,y in [(i+a, j+b) for a,b in dirs]:
                if 0 <= x < m and 0 <= y < n and graph[x][y] == 1:
                    dsu.union(x*n + y, i*n + j)
            out.append(dsu.num_sets - zeros)

        return out
                

        