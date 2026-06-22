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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        A = []
        for i,(u,v,w) in enumerate(edges):
            A.append([w,u,v,i])
        A.sort()

        def mst(idx, shouldSkip):
            dsu = DisjointSetUnion(n)
            ssum = 0
            if not shouldSkip:
                #if we aren't skipping it, then it means we're forcing it
                for i in range(len(A)):
                    if A[i][3] == idx:
                        ssum+=A[i][0]
                        dsu.union(A[i][1], A[i][2])
                        break
            for i in range(len(A)):
                if A[i][3] == idx and shouldSkip:
                    continue
                w,u,v = A[i][:3]
                if dsu.find(u) == dsu.find(v):
                    continue
                dsu.union(u,v)
                ssum+=w
            
            if len(dsu) != 1:
                return -1
            return ssum
                

        base = mst(-1, False)

        out = [set(), set()]
        for i in range(len(edges)):
            usedCost = mst(i, False)
            skipCost = mst(i, True)

            if usedCost == base and (skipCost > base or skipCost == -1):
                #if we use it and get an MST, but then skip it and don't get an MST, it's required
                out[0].add(i)
            elif usedCost == base and skipCost == base:
                #if we can use it or not use it and get the same answer, it's pseud
                out[1].add(i)
        return [list(x) for x in out]
