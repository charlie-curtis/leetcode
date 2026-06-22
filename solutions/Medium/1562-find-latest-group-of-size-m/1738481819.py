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
    def findLatestStep(self, A: List[int], m: int) -> int:


        goods = []
        seen = set()
        n = len(A)
        dsu = DisjointSetUnion(n)
        best = -1 
        for i,x in enumerate(A):
            x-=1
            seen.add(x)
            if x-1 in seen:
                dsu.union(x-1, x)
            if x+1 in seen:
                dsu.union(x+1, x)

            if dsu.set_size(x) == m:
                goods.append(x)
            
            while goods:
                r = dsu.find(goods[-1])
                if dsu.set_size(r) == m:
                    break
                else:
                    goods.pop()
            if goods:
                best = i+1
        return best

