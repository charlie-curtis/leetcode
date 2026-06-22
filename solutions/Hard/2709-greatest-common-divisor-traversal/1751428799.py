
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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        

        #if the input contains a 1, bail
        if 1 in nums:
            return len(nums) == 1
        def get_primes(x):
            cur = 2
            out = set()
            while cur*cur <= x:
                while x % cur == 0:
                    x//=cur
                    out.add(cur)
                cur+=1
            if x != 1:
                out.add(x)
            return out
        

        seen = {}
        n = len(nums)
        dsu = DisjointSetUnion(n)
        for i,x in enumerate(nums):
            for p in get_primes(x):
                if p in seen:
                    dsu.union(i, seen[p])
                else:
                    seen[p] = i
        return len(dsu) == 1

        

                
        