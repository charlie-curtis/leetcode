class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:

        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        n=0
        def dfs(x,prev, depth):
            nonlocal n
            n=max(n,depth)
            for nxt in adj[x]:
                if nxt!= prev:
                    dfs(nxt,x,depth+1)

        dfs(1,-1,1)

        mod=10**9+7
        print(n)

        return (pow(2,n-2,mod) + mod)%mod