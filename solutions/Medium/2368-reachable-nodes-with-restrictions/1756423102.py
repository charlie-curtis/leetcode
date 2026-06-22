class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        restricted = set(restricted)

        def dfs(x, prev):
            if x in restricted:
                return 0
            
            cnt = 1
            for nxt in adj[x]:
                if nxt != prev:
                    cnt+=dfs(nxt, x)
            return cnt
        

        return dfs(0, -1)

        