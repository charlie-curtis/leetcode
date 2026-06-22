class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        #editorial
        #tarjans algo

        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        disc = [-1]*n
        low = [-1]*n
        t = 0
        ans = []
        def dfs(node, prev):
            nonlocal t
            t+=1
            disc[node] = t
            low[node] = t

            for nxt in adj[node]:
                if nxt == prev:
                    continue
                if disc[nxt] == -1:
                    dfs(nxt, node)
                    low[node] = min(low[node], low[nxt])
                    if low[nxt] > disc[node]:
                        ans.append([node, nxt])
                else:
                    low[node] = min(low[node], low[nxt])

        dfs(0, -1)
        return ans
