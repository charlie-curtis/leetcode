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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        dsu = DisjointSetUnion(n+1)
        edges = []
        for u,v,w in pipes:
            edges.append([w,v,u])

        #this is an editorial approach where you add virtual edges and then do MST
        #my original approach didn't use virtual vertices, and it worked too.
        for i,x in enumerate(wells):
            edges.append([x,0,i+1])

        edges.sort()
        ans = 0
        for w,u,v in edges:
            r1, r2 = dsu.find(u), dsu.find(v)
            if r1 == r2:
                continue
            dsu.union(r1, r2)
            ans+=w
        return ans