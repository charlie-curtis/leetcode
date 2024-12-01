class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        d = defaultdict(list)
        d2 = defaultdict(list)
        n,m = len(edges1)+1, len(edges2)+1

        for u,v in edges1:
            d[u].append(v)
            d[v].append(u)

        for u,v in edges2:
            d2[u].append(v)
            d2[v].append(u)


        def dfs(node, isEven, seen, graph):

            if node in seen:
                return [0,0]
            seen.add(node)

            evens = 1 if isEven else 0
            odds = 0 if isEven else 1
            for u in graph[node]:
                t_evens, t_odds = dfs(u, not isEven, seen, graph)
                odds+=t_odds
                evens+=t_evens

            return [evens, odds]


        def dfs2(node, cur, seen, graph, res):
            if node in seen:
                return
            seen.add(node)

            res[node] = cur
            for u in graph[node]:
                dfs2(u, cur+1, seen, graph, res)


        evens1, odds1 = dfs(0, True, set(), d)
        evens2, odds2 = dfs(0, True, set(), d2)

        res1 = [0]*n
        res2 = [0]*m

        dfs2(0, 0, set(), d, res1)
        dfs2(0, 0, set(), d2, res2)

        #print(res1)
        best = max(evens2, odds2)

        out = [0]*n
        for i in range(n):
            if res1[i] % 2 == 0:
                out[i] = evens1 + best
            else:
                out[i] = odds1 + best
        return out
                