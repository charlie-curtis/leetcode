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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:



        dsuA = DisjointSetUnion(n)
        dsuB = DisjointSetUnion(n)

        edges.sort(key=lambda x: -x[0])

        used = 0
        for t,u,v in edges:
            u-=1
            v-=1
            if t == 3:
                need = dsuA.find(u) != dsuA.find(v) or dsuB.find(u) != dsuB.find(v)

                if need:
                    used+=1
                    dsuA.union(u,v)
                    dsuB.union(u,v)
                    
            if t == 1:
                need = dsuA.find(u) != dsuA.find(v)

                if need:
                    used+=1
                    dsuA.union(u,v)

            if t == 2:
                need = dsuB.find(u) != dsuB.find(v)

                if need:
                    used+=1
                    dsuB.union(u,v)

        if len(dsuB) == len(dsuA) == 1:
            return len(edges) - used
        return -1