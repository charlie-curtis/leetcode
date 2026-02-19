class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:


        n = len(s)
        uf = UnionFind(n)

        for x,y in pairs:
            uf.union(x,y)
        roots = defaultdict(list)
        for i,x in enumerate(s):
            roots[uf.find(i)].append(x)
        
        for k,v in roots.items():
            roots[k] = sorted(v, reverse=True)
        
        out = []
        for i in range(n):
            r = uf.find(i)
            out.append(roots[r].pop())
        return "".join(out)
