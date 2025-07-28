class Solution:
    def isPossibleToCutPath(self, g: List[List[int]]) -> bool:

        m,n = len(g), len(g[0])

        #got this one on my own. General idea is
        #1. remove any 1s from the graph that don't actually have a path to (m-1, n-1)
        #2. do a BFS from the start node. Process step by step (e.g. process all the paths that are 1 hop away from start, then 2, ... etc)
        #if at any point those BFS paths converge on a single node, then return true (aka you can remove that node and break the graph)

        @cache
        def reachable(i,j):
            if i == m-1 and j == n-1:
                return True
            if i < 0 or j < 0 or i ==m or j == n:
                return False
            return g[i][j] and (reachable(i+1,j) or reachable(i,j+1))


        for i in range(m):
            for j in range(n):
                if not reachable(i,j):
                    g[i][j] = 0

        if not reachable(0,0):
            return True

        reachable.cache_clear()
        q = [(0,0)]
        while q:
            seen = set()
            nxt = set()
            for _ in range(len(q)):
                i,j = q.pop()

                if (i,j) not in [(0,0), (m-1, n-1)]:
                    seen.add((i,j))

                if i + 1 < m and g[i+1][j]:
                    nxt.add((i+1,j))
                if j + 1 < n and g[i][j+1]:
                    nxt.add((i,j+1))
            
            if len(seen) == 1:
                return True
            q = list(nxt)
        return False
        