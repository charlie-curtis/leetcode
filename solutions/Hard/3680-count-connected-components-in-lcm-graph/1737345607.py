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
    def countComponents(self, nums: List[int], threshold: int) -> int:

        d = defaultdict(int)
        n = len(nums)
        dsu = DisjointSetUnion(n)

        d = {}
        for i,x in enumerate(nums):
            d[x] = i

        reachable = {}

        nums.sort()
        for x in range(1, threshold+1):
            if x not in d:
                continue
            if x in reachable:
                #print("Joining", d[x], reachable[x])
                dsu.union(d[x], reachable[x])
                continue
            t = x
            while t <= threshold:
                if t in reachable:
                    #print("JoiningAA", d[x], reachable[x])
                    dsu.union(d[x], reachable[t])
                else:
                    #print('setting', t, "to be reachable by", x)
                    reachable[t] = d[x] 
                t+=x

        return len(dsu)