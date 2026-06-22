class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        V=[False]*n
        ans=0
        def dfs(node):
            if V[node]:
                return 0
            V[node] = True
            cnt = 1
            for nxt in adj[node]:
                cnt+=dfs(nxt)
            return cnt
            
        for i in range(n):
            if not V[i]:
                L= dfs(i)
                ans+=L*(n-L)
        return ans//2
        