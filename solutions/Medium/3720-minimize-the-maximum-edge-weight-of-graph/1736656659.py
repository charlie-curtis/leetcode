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
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:

        d = defaultdict(list)

        for u,v,c in edges:
            d[v].append((u,c))

        pq = []
        for u,c in d[0]:
            heappush(pq, (c, u))

        V = set()
        V.add(0)
        best = 0
        while pq:
            cost, node = heappop(pq)
            if node in V:
                continue
            best = max(best, cost)
            V.add(node)

            for v,nc in d[node]:
                heappush(pq, (nc, v))


        for i in range(n):
            if i not in V:
                return -1
        return best
        