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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        dsu = DisjointSetUnion(n)

        pq = [[0,0]]

        def getdst(j):

            x1,y1 = points[j]
            A = []
            for i in range(n):
                if i == j:
                    continue
                x2,y2 = points[i]
                A.append([abs(x1-x2) + abs(y1-y2), i])
            return A

        ans = 0
        A = getdst(0)
        for dst, x in A:
            heappush(pq, [dst,x])
        while len(dsu) > 1:
            d, cur = heappop(pq)
            if dsu.find(0) == dsu.find(cur):
                continue
            dsu.union(0, cur)
            ans+=d
            for d, x in getdst(cur):
                if dsu.find(x) != dsu.find(0):
                    heappush(pq, [d, x])
        return ans
            
                
        