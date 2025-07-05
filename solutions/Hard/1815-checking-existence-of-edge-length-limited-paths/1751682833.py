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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], tmpqueries: List[List[int]]) -> List[bool]:

        #union find
        #offline processing of queries, sort them

        #if two nodes belong to the same connected component for the partially constructed graph, then
        #there is a path between the two using only weights strictly less than k


        dsu = DisjointSetUnion(n)
        edges = []
        for u,v,w in edgeList:
            edges.append([w,u,v])
        edges.sort()
        edges = deque(edges)
        queries = []
        for i, [u,v,limit] in enumerate(tmpqueries):
            queries.append([limit,u,v, i])
        queries.sort()

        out = [False]*len(queries)
        for limit,u1,v1,idx in queries:
            #print("Querying with limit", limit)
            while edges and edges[0][0] < limit:
                w,u,v = edges.popleft()
                #print("connecting", u,v, "with weight of", w)
                dsu.union(u,v)
            out[idx] = dsu.find(u1) == dsu.find(v1)
            #print("out", idx, "is", out[idx])
        return out
            



        
        