class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        colors = [-1]*n
        def dfs(x, color):
            if colors[x] != -1:
                return colors[x] == color
            
            if colors[x] == color:
                return True
            
            colors[x] = color
            res = True
            for nxt in graph[x]:
                res&=dfs(nxt, 1-color)
                if not res:
                    return False
            return True

        res = True
        for i in range(n):
            if colors[i] == -1:
                res&=dfs(i,0)
        return res
        