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
    def gcdSort(self, nums: List[int]) -> bool:
        
        @cache
        def getpfs(x):
            i=2
            out=set()
            while i*i <= x:
                while x%i==0:
                    out.add(i)
                    x//=i
                i+=1 if i==2 else 2
            if x!=1: out.add(x)
            return out
        
        d ={}
        n=len(nums)
        dsu=DisjointSetUnion(n)
        for i,x in enumerate(nums):
            for pf in getpfs(x):
                if pf in d:
                    dsu.union(i, d[pf])
                else: d[pf] = i
        A = [(x,i) for (i,x) in enumerate(nums)]
        A.sort()
        for i,(_,j) in enumerate(A):
            if dsu.find(i) != dsu.find(j): return False
        return True
        