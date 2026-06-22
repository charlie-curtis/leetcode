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
class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):

        dsu = DisjointSetUnion(n)
        d = defaultdict(set)
        for u,v,w in edgeList:
            d[w].add((u,v))

        A = []
        B = []

        for k in sorted(d.keys()):
            for u,v in d[k]:
                dsu.union(u,v)
            A.append(k)
            B.append(copy.deepcopy(dsu))
        
        self.A = A
        self.B = B

    def query(self, p: int, q: int, limit: int) -> bool:
        idx = bisect_left(self.A, limit)-1
        if idx == -1:
            return False
        dsu = self.B[idx]
        return dsu.find(p) == dsu.find(q)
        


# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)