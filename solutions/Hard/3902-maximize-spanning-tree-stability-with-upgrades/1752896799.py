#DSU Template from PYRIVAL
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
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        #maximal spanning tree
        #start w/ all the nodes where must = 1

        dsu = DisjointSetUnion(n)
        q = []
        INF = 2*10**9
        ans = INF
        for u,v, si, must in edges:
            if must:
                if dsu.find(u) == dsu.find(v):
                    return -1
                dsu.union(u,v)
                ans = min(si, ans)
            else:
                q.append([-si, u,v])
        
        if dsu.num_sets == 1:
            return ans
        options = []
        q.sort()
        for si,u,v in q:
            si = -si
            if dsu.find(u) != dsu.find(v):
                options.append(si)
                dsu.union(u,v)
        if dsu.num_sets != 1:
            return -1
        if len(options) > k: #we can't double every value, so the answer will either be 1) the smallest value of MUST 2) the smallest value we could double 3) the smallest value we couldn't double
            ans = min(ans, 2*options[-k], options[-k-1])
        else:
            return min(ans, 2*options[-1]) #we can double every value not in MUST
        return ans