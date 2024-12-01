class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        d = defaultdict(list)
        d2 = defaultdict(list)
        n,m = len(edges1)+1, len(edges2)+1

        for u,v in edges1:
            d[u].append(v)
            d[v].append(u)

        for u,v in edges2:
            d2[u].append(v)
            d2[v].append(u)

        #print(d)

        def dfs(node, rem, seen, graph):

            if rem < 0 or node in seen:
                return 0
            seen.add(node)

            ans = 1
            for u in graph[node]:
                ans+=dfs(u, rem-1, seen, graph)
            return ans


        out = [0]*n
        for i in range(n):
            out[i] = dfs(i, k, set(), d)

        #print("OUT was", out)

        best = 0
        for i in range(m):
            best = max(best, dfs(i,k-1, set(), d2))

        #print("BEST was", best)

        return [x+best for x in out]

        
            
                