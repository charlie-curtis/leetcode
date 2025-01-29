class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        d = defaultdict(set)
        for a,b in edges:
            d[a].add(b)
            d[b].add(a)

        if len(edges) != n-1:
            return False

        
        seen = set()
        def dfs(cur):
            
            if cur in seen:
                return True
            
            seen.add(cur)
            for nxt in d[cur]:
                res = dfs(nxt)
                if not res:
                    return False
            return True

        return dfs(0) & (len(seen) == n)

