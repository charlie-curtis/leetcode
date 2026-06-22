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
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:

        if threshold == 0:
            return [True]*len(queries)

        dsu = DisjointSetUnion(n+1)
        def sieve(i):
            if i <= threshold or dsu.find(i) != i:
                return
            
            j = 2
            while True:
                if i*j > n:
                    break
                dsu.union(i,j*i)
                j+=1

        
        for i in range(1,n+1):
            sieve(i)


        out = []
        for u,v in queries:
            out.append(dsu.find(u) == dsu.find(v))
        return out






        