class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(set)
        for u,v in roads:
            adj[u].add(v)
            adj[v].add(u)


        ans = 0
        for i in range(n):
            A = set()
            for u in adj[i]:
                A.add(tuple(sorted([u,i])))
            s1 = adj[i]
            for j in range(i+1,n):
                A2 = set()
                for u in adj[j]:
                    A2.add(tuple(sorted([u,j])))
                    ans = max(ans, len(A|A2))
        return ans
                
        