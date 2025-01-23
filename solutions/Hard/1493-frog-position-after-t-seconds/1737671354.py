class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)



        ans = 0
        def dfs(node, k, parent, prob):
            nonlocal ans

            m = len(adj[node])
            if parent != -1:
                m-=1
            if m == 0 or k == t:
                if node == target:
                    ans = prob
                return

            for u in adj[node]:
                if u != parent:
                    dfs(u, k+1, node, prob/m)



        dfs(1, 0, -1, 1)
        return ans
        