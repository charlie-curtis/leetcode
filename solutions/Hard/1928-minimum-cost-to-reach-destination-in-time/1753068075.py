class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
        n = len(passingFees)

        INF = 10**9
        @cache
        def dp(i, t):
            if t > maxTime:
                return INF
            
            if i == n-1:
                return passingFees[i]
            
            can = INF
            for nxt,w in adj[i]:
                can = min(can, dp(nxt,t+w))
            
            return can + passingFees[i]

        res = dp(0, 0)
        if res >= INF:
            return -1
        return res
