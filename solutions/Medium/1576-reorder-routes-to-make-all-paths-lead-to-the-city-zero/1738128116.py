class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adj = defaultdict(set)

        for u,v in connections:
            adj[u].add((v, 1))
            adj[v].add((u, 0))

        def dfs(cur, p):
            ans = 0
            for u,w in adj[cur]:
                if u == p:
                    continue
                ans+=w
                ans+=dfs(u, cur)
        
            return ans
        return dfs(0, -1)