class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:

        d = defaultdict(set)
        for u,v in edges:
            d[u].add(v)
            d[v].add(u)


        def dfs(x, mmap, dst):
            if x in mmap:
                return
            
            mmap[x] = dst

            for y in d[x]:
                dfs(y, mmap, dst+1)


        m1 = {}
        dfs(0, m1, 0)
        endpoint = -1

        endpoint = sorted([(-y,x) for (x,y) in m1.items()])[0][1]

        m1 = {}
        dfs(endpoint, m1, 0)
        endpoint2 = sorted([(-y,x) for (x,y) in m1.items()])[0][1]

        m2 = {}
        dfs(endpoint2, m2, 0)

        out = []
        for i in range(len(edges)+1):
            if m1[i] > m2[i]:
                out.append(endpoint)
            else:
                out.append(endpoint2)
        return out



            
        