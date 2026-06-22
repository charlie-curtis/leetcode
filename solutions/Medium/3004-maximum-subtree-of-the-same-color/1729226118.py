class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:

        d = defaultdict(set)
        for u,v in edges:
            d[u].add(v)
            d[v].add(u)

        ans = 0
        seen = set()
        def dfs(node):
            nonlocal ans

            if node in seen:
                return 0
            seen.add(node)

            color = colors[node]
            total_nodes = 1
            good = True
            for x in d[node]:
                if x in seen:
                    continue
                nodes = dfs(x)
                if nodes == -1 or colors[x] != color:
                    good = False
                total_nodes+=nodes

            if good:
                ans = max(ans, total_nodes)
            
            return total_nodes if good else -1
                
        dfs(0)
        return ans